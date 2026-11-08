"""
RECORD CHECK  -  my version
===========================

Name  :terrell
Lane  :  Cyber
Date  :2026-11-8

Checks as many records as you like in one run. For each source IP it asks for
the failed logins and total attempts, prints a bordered report with the status,
and counts how many came back OVER LIMIT. Type "quit" as the source IP to stop.

Run it:   python template.py
"""


# ================================================================== FUNCTIONS
def status_of(percent):
    """Return "OVER LIMIT", "WARNING" or "OK" for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and the percentage of value against limit."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


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


over_limit_count = 0

while True:
    # ================================================================== INPUT
    source_ip = input("Source IP (or 'quit') : ")
    if source_ip == "quit":
        break

    failed_logins  = float(input("Failed logins         : "))
    total_attempts = float(input("Total attempts        : "))

    # ================================================================ PROCESS
    difference, percent = check(failed_logins, total_attempts)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # ================================================================= OUTPUT
    print_report(source_ip, failed_logins, total_attempts, difference, percent, status)

print(f"Sources over limit: {over_limit_count}")