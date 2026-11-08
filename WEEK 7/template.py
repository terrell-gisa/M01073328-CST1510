"""
RECORD CHECK  -  my version
===========================

Name  :  terrell
Lane  :  Cyber Security
Date  :  2026-11-08

Run it:   python template.py     (from inside the LAB folder)

"""
import os
RECORDS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "records.txt")

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Turn one messy raw login line into a clean dict."""
    line = raw_line.strip().lower()

    fields = {}
    for piece in line.split(","):
        key, value = piece.split("=")# ValueError: too many values to unpack
        fields[key.strip()] = value.strip()# clean the text first ...

    return {
        "src": fields["src"], # KeyError if the field is missing
        "attempts": int(fields["attempts"]),# ... then convert (ValueError if not a number)
        "result": fields["result"],
    }


def status_of(attempts, result, flag_at=10):
    """Return FLAGGED for failed logins at or over flag_at attempts, otherwise OK."""
    if result == "failed" and attempts >= flag_at:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
# Raw, messy records are saved in records.txt (varied spacing and case, plus
# one deliberately bad line to test the error handling). The file is read
# line by line in the loop below.


# =============================================================== PROCESS + OUTPUT
total_records = 0
flagged = 0
skipped = 0

print(f"{'SRC':<16} {'ATTEMPTS':<9} {'RESULT':<9} STATUS")
print("-" * 44)

with open(RECORDS_FILE) as f:
    for raw_line in f:
        if raw_line.strip() == "":# ignore blank lines
            continue
        try:
            record = parse_line(raw_line)
        except (ValueError, KeyError):
            print(f"Could not parse: {raw_line.strip()}")
            skipped += 1
            continue

        status = status_of(record["attempts"], record["result"])
        total_records += 1
        if status == "FLAGGED":
            flagged += 1
        print(f"{record['src']:<16} {record['attempts']:<9} {record['result']:<9} {status}")

print(f"\nSummary: {total_records} records parsed, {flagged} flagged, {skipped} could not be parsed.")


