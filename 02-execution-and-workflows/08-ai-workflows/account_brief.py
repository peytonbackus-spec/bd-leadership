import sys
import json

def generate_brief(account_name, industry, revenue):
    brief = {
        "account": account_name,
        "industry": industry,
        "revenue": revenue,
        "summary": f"{account_name} operates in {industry} with estimated revenue of {revenue}.",
        "recommended_angle": "Focus on pipeline efficiency and automated workflow integration."
    }
    return json.dumps(brief, indent=2)

if __name__ == '__main__':
    account = sys.argv[1] if len(sys.argv) > 1 else "Acme Corp"
    print(generate_brief(account, "Enterprise Software", "$150M"))
