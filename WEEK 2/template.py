"""
RECORD CHECK  -  my version
===========================

Name  :terrell
Lane  :   Cyber     (delete two)
Date  :25/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

## ==================================================================== INPUT

hostname = input("Hostname: ")
used = float(input("GB used: "))
total = float(input("GB total: "))


# ================================================================== PROCESS

free = total - used
percent = (used / total) * 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

print(f"  Used        : {used:>10.2f}")
print(f"  Total       : {total:>10.2f}")
print(f"  Free        : {free:>10.2f}")
print(f"  Percent     : {percent:>10.2f} %")
print(f"  Status      : {status:>10}")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
