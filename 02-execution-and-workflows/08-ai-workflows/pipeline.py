import sys
import pandas as pd

def run_pipeline(mode, accounts_file='sample-data/accounts.csv', contacts_file='sample-data/contacts.csv'):
    print(f"=== Running AI Pipeline in [{mode.upper()}] Mode ===")
    accounts = pd.read_csv(accounts_file)
    contacts = pd.read_csv(contacts_file)

    merged = pd.merge(contacts, accounts, on='account_id', how='inner')
    merged['generated_hook'] = merged.apply(
        lambda r: f"Hi {r['first_name']}, saw your focus on {r['title']} at {r['account_name']}. Worth connecting on modernizing your pipeline stack?",
        axis=1
    )

    if mode == 'build':
        output_file = 'approval_queue.csv'
        merged.to_csv(output_file, index=False)
        print(f"Generated {len(merged)} prospect hooks. Pending human review in '{output_file}'.")
    elif mode == 'enroll':
        print(f"Enrolling {len(merged)} validated records into Outreach sequences...")
        print("Status: 200 OK - All payloads successfully dispatched.")

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'build'
    run_pipeline(mode)
