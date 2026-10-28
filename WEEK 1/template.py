"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT

label = input("Record ID: ")
first = float(input("Value: "))
second = float(input("Limit: "))


# ================================================================== PROCESS

difference = first - second
percent = (first / second) * 100


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Value      : {first:>10.2f}")
print(f"Limit      : {second:>10.2f}")
print(f"Difference : {difference:>10.2f}")
print(f"Percent    : {percent:>10.2f}%")

print("=" * 34)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
