import sys
import pandas as pd

def backtest():
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'sample-data/historical.csv'
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error loading {input_file}: {e}")
        return

    print("=== Conversion Rate Backtest by Score Tier ===")
    tier_summary = df.groupby('tier').agg(
        total_accounts=('account_id', 'count'),
        converted_opps=('converted', 'sum')
    )
    tier_summary['conversion_rate'] = (tier_summary['converted_opps'] / tier_summary['total_accounts'] * 100).round(2).astype(str) + '%'
    print(tier_summary)

if __name__ == '__main__':
    backtest()
