"""
RECORD CHECK  -  my version
===========================

Name  :terrell
Lane  :  Cyber       (delete two)
Date  :25/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

class Record:
    def __init__(self, label, value, limit):
        """Initialize a record with its label, value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the value and limit."""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS

record1 = Record("R001", 87, 100)
record2 = Record("R002", 120, 100)

records = [record1, record2]


# ==================================================================== OUTPUT

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print("  Value  :", record.value)
    print("  Limit  :", record.limit)
    print("  Status :", record.status())

    print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
