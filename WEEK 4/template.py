"""
RECORD CHECK  -  my version
===========================

Name  :terrell
Lane  :  Cyber      (delete two)
Date  :25/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


from pathlib import Path


# =================================================================== FUNCTIONS

def check_record(value, limit, warning_at=90):
    """Work out the difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= warning_at:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


# ====================================================================== STORE

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / "records_sample.txt"

records = []

try:
    with open(file_path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

except FileNotFoundError:
    print("records_sample.txt not found")


# =============================================================== PROCESS + OUTPUT

for record in records:
    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print(f"{record['label']}:")
    print(f"  Value: {record['value']:.2f}")
    print(f"  Limit: {record['limit']:.2f}")
    print(f"  Difference: {difference:+.2f}")
    print(f"  Percentage: {percent:.1f}%")
    print(f"  Status: {status}")
    print()
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
