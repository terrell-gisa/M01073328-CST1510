"""
RECORD CHECK  -  my version
===========================

Name  :terrell
Lane  :  Cyber
Date  :2026-11-8

Checks as many records as you like in one run. For each source IP it asks for
the failed logins and total attempts, decides a status, prints a bordered
report and counts how many came back OVER LIMIT. Type "quit" as the source IP
to stop.

Run it:   python template.py
"""

over_limit_count = 0

while True:
    # ================================================================== INPUT
    source_ip = input("Source IP (or 'quit') : ")
    if source_ip == "quit":
        break

    failed_logins  = float(input("Failed logins         : "))
    total_attempts = float(input("Total attempts        : "))

    # ================================================================ PROCESS
    successful_logins = total_attempts - failed_logins
    failed_percent    = (failed_logins / total_attempts) * 100

    if failed_percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif failed_percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # ================================================================= OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {source_ip}")
    print("=" * 34)
    print(f"  Failed      : {failed_logins:>10.2f}")
    print(f"  Attempts    : {total_attempts:>10.2f}")
    print(f"  Successful  : {successful_logins:>10.2f}")
    print(f"  Failed %    : {failed_percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

print(f"Sources over limit: {over_limit_count}")