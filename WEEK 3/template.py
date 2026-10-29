"""
RECORD CHECK  -  my version
===========================

Name  :Gisa Terrell
Lane  :  Cyber     (delete two)
Date  :22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. 
# 
def status_of(percent):
    """Return the status based on the given percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate and return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a report showing the value, limit, difference, percentage, and status."""
    print(f"label: {label}")
    print(f"value: {value}")
    print(f"limit: {limit}")
    print(f"difference: {difference}")
    print(f"percentage: {percent:.2f}%")
    print(f"status: {status}")

# ==================================================================== INPUT
# 2. Ask for your three values.

label = input("Enter a name, hostname, or IP: ")
value = float(input("Enter the value: "))
limit = float(input("Enter the limit: "))


# ================================================================== PROCESS
# 3.
difference = value - limit
percent = (value / limit) * 100
status = status_of(percent)


# =================================================================== OUTPUT
# 4. Print the report.


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"value: {value:.2f}")
print(f"limit: {limit:.2f}")
print(f"difference: {difference:.2f}")
print(f"percent: {percent:.2f}%")
print(f"status: {status}")
print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
