"""
RECORD CHECK  -  my version
===========================

Name  :  Terrell
Lane  :  Cyber Security
Date  :  2026-11-08

Run it:   python template.py

Checks the login attempts from each source IP. For every IP it works out the
percent of attempts that failed and gives it a status (OK / WARNING / OVER LIMIT),
then reports the suspicious IPs, a count per status, a saved CSV and a bar chart.

"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==================================================================== LOAD
here = Path(__file__).parent
df = pd.read_csv(here / "cyber_logins.csv")


# ================================================================= PROCESS
# percent of attempts that failed for each IP
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

# status from the percent: 100 OVER LIMIT, 90+ WARNING, otherwise OK
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT
print("ALL SOURCE IPs")
print(df)
print("\nSUSPICIOUS IPs (status is not OK)")
print(df[df["status"] != "OK"])
print("\nCOUNT PER STATUS (groupby)")
print(df.groupby("status")["source_ip"].count())
df.to_csv(here / "login_report.csv", index=False)
print("\nSaved login_report.csv")
df["status"].value_counts().plot(kind="bar", title="Source IPs by login status")
plt.xlabel("Status")
plt.ylabel("Number of IPs")
plt.tight_layout()
plt.savefig(here / "login_status_counts.png")
print("Saved login_status_counts.png")


