import sys
import pandas as pd

def score_account(row):
    score = 0
    # Firmographic Fit
    employees = float(row.get('employees', 0))
    if 250 <= employees <= 5000:
        score += 30
    elif employees > 5000:
        score += 20

    revenue = float(row.get('revenue_m', 0))
    if 50 <= revenue <= 1000:
        score += 30
    elif revenue > 1000:
        score += 20

    # Tech Stack & Signal Fit
    if str(row.get('has_salesforce', '')).strip().lower() in ['true', '1', 'yes']:
        score += 20
    if str(row.get('hiring_signal', '')).strip().lower() in ['true', '1', 'yes']:
        score += 20

    return score

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'sample-data/accounts.csv'
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error loading {input_file}: {e}")
        return

    df['fit_score'] = df.apply(score_account, axis=1)
    df['tier'] = df['fit_score'].apply(lambda s: 'Tier 1' if s >= 80 else ('Tier 2' if s >= 50 else 'Tier 3'))

    print("=== Account Scoring Summary ===")
    print(df[['account_name', 'employees', 'revenue_m', 'fit_score', 'tier']])
    df.to_csv('sample-data/scored_accounts.csv', index=False)
    print("\nSaved scored output to sample-data/scored_accounts.csv")

if __name__ == '__main__':
    main()
