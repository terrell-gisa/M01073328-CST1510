"""
RECORD CHECK  -  my version
===========================

Name  : terrell gisa
Lane  :  Cyber      
Date  :10/3/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT

label = input("enter a name, a hostname, an IP ")     
first = float(input("write the first number "))    
second = float(input("write the second number "))    


# ================================================================== PROCESS

difference = first-second   # 
percent = first/second*100      # 
print(difference)
print(f"{percent:>10.2f}"+"%")

# =================================================================== OUTPUT


print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here
print(f"{difference:>+10.2f}")
print(f"{percent:>10.2f}"+"%")

print("=" * 34)


