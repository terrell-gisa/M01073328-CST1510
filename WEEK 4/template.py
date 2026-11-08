"""
RECORD CHECK  -  my version
===========================

Name  :terrell
Lane  :  Cyber
Date  :2026-11-8

Loads source IP records (label,value,limit - the IP, failed logins and total
attempts) from cyber_records.txt, checks and reports on each one, writes
label,status lines to results.txt and prints how many came back OVER LIMIT.
A missing data file prints a clear message instead of crashing.

Run it:   python template.py
"""

# ================================================================== FUNCTIONS
def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records


def check_record(value, limit):
    """Return the difference, percentage and status for one record."""
    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered report - only shows values, calculates nothing."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Failed      : {value:>10.2f}")
    print(f"  Attempts    : {limit:>10.2f}")
    print(f"  Successful  : {difference:>10.2f}")
    print(f"  Failed %    : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def write_results(path, results):
    """Write one label,status line per result to a new file."""
    with open(path, "w") as f:
        for result in results:
            f.write(f"{result['label']},{result['status']}\n")


# ====================================================================== STORE
try:
    records = load_records("cyber_records.txt")
except FileNotFoundError:
    print("Could not find cyber_records.txt - starting with no records.")
    records = []


# =========================================================== PROCESS + OUTPUT
over_limit_count = 0
results = []

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    results.append({"label": record["label"], "status": status})

    if status == "OVER LIMIT":
        over_limit_count += 1

write_results("results.txt", results)
print(f"Checked {len(records)} records. {over_limit_count} were over limit.")