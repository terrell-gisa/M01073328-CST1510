"""
RECORD CHECK  -  my version
===========================

Name  :Terrell
Lane  :Cyber 
Date  :10/4/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.

label = input("Label: ")      
value = float(input("Value: "))     
limit = float(input("Limit: "))     

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = value - limit   
percent = (difference / limit * 100)       
# 3. Decide a status and store it in a variable called status.

status = "OVER LIMIT" if value > limit else "OK"


# =================================================================== OUTPUT
# 4. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here
print(f"  value:      {value:>10.2f}")
print(f"  limit:      {limit:>10.2f}")
print(f"  status:     {status:>10}")
print(f"  difference: {difference:>+10.2f}")
print(f"  percentage: {percent:>10.2f}" , "%")
print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
