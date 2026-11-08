"""
RECORD CHECK  -  my version
===========================

Name  :terrell
Lane  :  Cyber
Date  :2026-11-8

Loads source IP records (label,value,limit - the IP, failed logins and total
attempts) from cyber_records.txt as Record objects, prints a bordered report
with the status for each one and counts how many came back OVER LIMIT.

Run it:   python template.py
"""

# ====================================================================== CLASS
class Record:
    """One source IP: its failed logins measured against its total attempts."""

    def __init__(self, label, value, limit):
        """Store the label, failed logins (value) and total attempts (limit)."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return "OVER LIMIT", "WARNING" or "OK" for this record."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


# ==================================================================== RECORDS
records = load_records("cyber_records.txt")


# ===================================================================== OUTPUT
over_limit_count = 0

for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Failed      : {record.value:>10.2f}")
    print(f"  Attempts    : {record.limit:>10.2f}")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"Checked {len(records)} records. {over_limit_count} were over limit.")