"""
RECORD CHECK  -  my version
===========================

Name  :terrell
Lane  :  Cyber
Date  : 2026-11-8

Run it:   python template.py
"""

# ==================================================================== INPUT
# input() always gives back text, so the two numbers are converted with float().
source_ip      = input("Source IP       : ")
failed_logins  = float(input("Failed logins   : "))
total_attempts = float(input("Total attempts  : "))


# ================================================================== PROCESS
# Everything below is calculated from what the user typed - nothing is typed in.
successful_logins = total_attempts - failed_logins
failed_percent    = (failed_logins / total_attempts) * 100

# Extra line (Excellent): failed logins ABOVE a "normal" failure rate.
# Why: a few failed logins are normal (typos, expired passwords), so the raw count
# on its own tells an analyst very little. What matters is how far a source sits
# above normal. Positive = over the baseline (worth chasing up), negative = within it.
# 5 is an assumed baseline - change it to suit.
normal_failure_percent = 5
excess_failures = failed_logins - (total_attempts * normal_failure_percent / 100)


# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 34)
print(f"  Failed      : {failed_logins:>10.2f}")
print(f"  Attempts    : {total_attempts:>10.2f}")
print(f"  Successful  : {successful_logins:>+10.2f}")
print(f"  Failed %    : {failed_percent:>10.2f} %")
print(f"  Over normal : {excess_failures:>+10.2f}")
print("=" * 34)