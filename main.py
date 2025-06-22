import argparse
import requests
import json
from datetime import datetime
import pandas as pd
from pathlib import Path

LOG_FILE = Path("logs/log.json")
DATA_FILE = Path("data/rates.xlsx")

def fetch_rate(base, target):
    url = f"https://open.er-api.com/v6/latest/{base}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None

    if data.get("result") == "success":
        rate = data["rates"].get(target)
        if rate:
            print(f"💱 1 {base} = {rate} {target}")
            return rate
        else:
            print(f"❌ Target currency {target} not found")
            return None
    else:
        print(f"❌ API error: {data.get('error-type')}")
        return None

def save_to_excel(base, target, rate):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame([{
        "timestamp": now,
        "base_currency": base,
        "target_currency": target,
        "rate": rate
    }])

    if DATA_FILE.exists():
        existing = pd.read_excel(DATA_FILE)
        df = pd.concat([existing, df], ignore_index=True)

    df.to_excel(DATA_FILE, index=False)
    print(f"✅ Saved to {DATA_FILE}")

def log_result(base, target, rate):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "base_currency": base,
        "target_currency": target,
        "rate": rate
    }
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def show_log():
    if not LOG_FILE.exists():
        print("No log found.")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            print(f"{entry['timestamp']} | {entry['base_currency']} -> {entry['target_currency']} : {entry['rate']}")

def main():
    parser = argparse.ArgumentParser(description="Currency Rate Fetcher")
    parser.add_argument("--currency", type=str, required=True, help="Base currency code (e.g. USD)")
    parser.add_argument("--target", type=str, required=True, help="Target currency code (e.g. EUR)")
    parser.add_argument("--save", action="store_true", help="Save result to Excel")
    parser.add_argument("--log", action="store_true", help="Show log")

    args = parser.parse_args()

    if args.log:
        show_log()
        return

    rate = fetch_rate(args.currency, args.target)
    if rate is not None:
        log_result(args.currency, args.target, rate)
        if args.save:
            save_to_excel(args.currency, args.target, rate)

if __name__ == "__main__":
    main()
