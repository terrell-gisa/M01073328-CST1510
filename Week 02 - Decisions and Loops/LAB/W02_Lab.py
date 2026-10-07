# Week 2 — Lab

**3 hours.** Work through in order. You are not expected to finish everything.

| Part | Time | What |
|---|---|---|
| Warm-up | 15 min | Fix three broken programs |
| Drills | 60 min | Short tasks on every topic this week, plus two challenges |
| Break | 10 min | |
| Mini-project | 80 min | Add decisions and a loop to your Record Check |
| Wrap-up | 15 min | Cheat sheet notes, photo, push to GitHub |

**Aiming for a pass?** Do all the drills in Topics 1–4 and the Threshold version of the mini-project.
**Aiming higher?** Add the Typical version of the mini-project.
**Aiming for a first?** Add the two Challenge drills and the Excellent version of the mini-project.

> ### What you submit this week
> Both files stay in this `LAB` folder and are pushed to GitHub at the end of the lab.
>
> 1. **This notebook**, with your drill answers and the photo of your Cheat Sheet pasted in at the very end
> 2. **`template.py`**, your completed mini-project
>
> The warm-up is not submitted.

> ### If you are stuck
> 1. Read the **last line** of the error. If there is no error, check what should be stopping your loop.
> 2. Check the *Common mistakes* table in that topic's walkthrough.
> 3. Run the matching file in that topic's `examples/` folder.
> 4. Ask, and say what the last line of the error said.
---
# Warm-up · 15 min

Open the `warmup/` folder. Each file is **broken on purpose**. For each one:

1. Run it and read the **last line** of the error first.
2. Look at the line number it gives you.
3. Fix it and run it again.

| Error you will meet | Usually means |
|---|---|
| `IndentationError` | the line under `if`, `while` or `for` is not indented |
| `SyntaxError` | often a missing `:` at the end of an `if`, `while` or `for` line |
| `TypeError` | comparing text with a number: did you forget `float()`? |
---
# Drills

The drills follow the four topics from the workshop, in the same order. Each one is short and
tests one idea. Run your cell and compare it with the expected output.

---
## Topic 1 · Comparisons and Boolean logic
*Walkthrough: `01 - Comparisons and Boolean Logic`*
### D1. The six comparison operators

1. Create `a = 10` and `b = 20`.
2. Print the result of each comparison: `a == b`, `a != b`, `a < b`, `a > b`, `a <= b`, `a >= b`

**Expected output:** `False`, `True`, `True`, `False`, `True`, `False` (one per line)
# D1
a=10
b=20
print(a==b)
print(a!=b) 
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
### D2. `=` stores, `==` asks

1. Store the number 50 in a variable called `limit`.
2. Print `limit == 50`, then print `limit == 60`.
3. Add a comment above each line saying whether it **stores** a value or **asks** a question.
**Expected output:** `True`, then `False`
a=10
b=20
print(a==b)
print(a!=b) 
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
 output
False
True
False
True
False
True
# D2
#this stores the 50 in the variable limit
limit = 50
print(limit == 50)
print(limit == 60)
output
True
False
### D3. A comparison is a value too

1. Create `attempts = 4` and `max_attempts = 3`.
2. Store the comparison in a variable: `is_locked = attempts >= max_attempts`
3. Print `is_locked`, then print `type(is_locked)`.

**Expected output:**
    # D3
attempts = 4
max_attempts = 3
is_locked = attempts > max_attempts
print(is_locked)
print(type(is_locked))
```
True
<class 'bool'>
### D4. Combining conditions with `and`, `or`, `not`

1. Create `percent = 95`.
2. Print each of these:
   - `percent >= 90 and percent < 100`
   - `percent < 50 or percent > 90`
   - `not (percent > 90)`

**Expected output:** `True`, `True`, `False`

Now change `percent` to `40` and run again. Before you run it, predict the three results.
# D4
percent = 95
print(percent >= 90 and percent < 100)
print(percent < 50 or percent > 100)
print(not percent >= 50)
output
True
False
False
---
## Topic 2 · `if`, `elif`, `else`
*Walkthrough: `02 - if, elif, else`*
### D5. `if` on its own

1. Create `value = 120` and `limit = 100`.
2. Use `if` to print `OVER LIMIT` when `value` is greater than `limit`.

**Expected output:** `OVER LIMIT`

Now change `value` to `80` and run again. Nothing is printed. Add a comment explaining why.
# D5
### D6. `if` / `else`

1. Create `value = 87` and `limit = 100`.
2. Use `if` / `else`:
   - if `value` is greater than `limit`, print `OVER LIMIT`
   - otherwise, print `OK`

**Expected output:** `OK`

Now change `value` to `120` and run again. You should see `OVER LIMIT`.
# D6
### D7. Three possible results with `if` / `elif` / `else`

1. Create `value = 87` and `limit = 100`.
2. Calculate the percentage: `percent = (value / limit) * 100`
3. Use `if` / `elif` / `else` to print:
   - `OVER LIMIT` if `percent` is 100 or more
   - `WARNING` if `percent` is 90 or more
   - `OK` otherwise

**Test it** by changing `value` and running the cell each time:

| value | Expected output |
|---|---|
| 87 | `OK` |
| 95 | `WARNING` |
| 120 | `OVER LIMIT` |

*Hint: check for 100 first. Python runs the first branch that is True and skips the rest.*
# D7
### D8. Indentation decides what is inside the `if`

The code is already in the cell below.

1. **Before you run it**, write a comment predicting what it will print.
2. Run it and check your prediction.
3. Now indent the last `print` line so it lines up with `print("OVER LIMIT")`. Run it again.
4. Add a comment explaining why the output changed.

**Expected output:** first `Check finished`, then (after step 3) nothing at all.
# D8
value = 50
limit = 100

if value > limit:
    print("OVER LIMIT")
print("Check finished")
---
## Topic 3 · `while` loops
*Walkthrough: `03 - while Loops`*
### D9. Count from 1 to 10 with `while`

1. Create a variable `count = 1`.
2. Write a `while` loop that runs while `count` is 10 or less.
3. Inside the loop, print `count`, then add 1 to it (`count += 1`).

**Expected output:** the numbers 1 to 10, one per line.
# D9
### D10. Fix the loop that never stops

The code below is broken: it would print `1` forever.

1. **Do not run it yet.** Read it and find why the condition never becomes False.
2. Fix it, then run it.

**Expected output:** the numbers 1 to 5, one per line.

*If a loop ever runs forever, click the stop button (■) at the top of the notebook.*
# D10
count = 1
while count <= 5:
    print(count)
### D11. `while True` and `break`: add numbers until the user types `done`

1. Create a variable `total = 0`.
2. Use a `while True:` loop. Inside it, ask: `Enter a number (or done to finish): `
3. If the user types `done`, stop the loop with `break`.
4. Otherwise, convert what they typed with `float()` and add it to `total`.
5. After the loop, print the total.

**Example run:**

```
Enter a number (or done to finish): 5
Enter a number (or done to finish): 10
Enter a number (or done to finish): 2.5
Enter a number (or done to finish): done
Total: 17.5
```

*In a notebook, the input box appears at the top of VS Code. Press Enter after each number.*
# D11
### D12. `continue`: skip one number

Use a `while` loop to print the numbers 1 to 10, but **skip 5** using `continue`.

**Expected output:** `1 2 3 4 6 7 8 9 10` (one per line)

*Hint: add 1 to your counter **before** the `continue`, or the loop gets stuck on 5.*
# D12
---
## Topic 4 · `for` loops and `range()`
*Walkthrough: `04 - for Loops and range`*
### D13. `range(stop)` and `range(start, stop)`

1. Use `for i in range(5):` to print the numbers it gives you.
2. Then write a second loop using `range(start, stop)` that prints 1 to 5.

**Expected output:** `0 1 2 3 4`, then `1 2 3 4 5` (one per line)

*Remember: the `stop` number is never included.*
# D13
### D14. `range(start, stop, step)`

1. Print every even number from 2 to 20.
2. Then write a second loop that counts down from 10 to 1.

**Expected output:** `2 4 6 … 20`, then `10 9 8 … 1` (one per line)

*Hint: to count down, use a negative step.*
# D14
### D15. `enumerate()`: the position and the value together

1. Create `code = "A7X"`.
2. Use a `for` loop with `enumerate(code, start=1)` to print each character with its position.

**Expected output:**
```
Character 1: A
Character 2: 7
Character 3: X
```
# D15
### D16. `for` or `while`?

Write both programs below. Above each one, add a comment saying which loop you chose and why.

a) Ask the user for **exactly 3** numbers, and print each one back.

b) Keep asking for a password until the user types `letmein`, then print `Welcome`.

*Hint: do you know in advance how many times the loop will run?*
# D16
---
## Challenge · for a first

*These combine several ideas from this week. There are no step-by-step instructions.*
### C1. Check three records in one run

Write a `for` loop that runs exactly 3 times. Each time, ask for a `value` and a `limit`,
and print `OVER LIMIT` if `value` is greater than `limit`, otherwise `OK`.

**Test it** with these three pairs, in this order:

| value | limit | Expected output |
|---|---|---|
| 87 | 100 | `OK` |
| 120 | 100 | `OVER LIMIT` |
| 45 | 100 | `OK` |
# C1
### C2. Three tries to log in

The correct password is `python123`. The user gets **at most 3 tries**.

- If they type the correct password, print `Access granted` and stop asking.
- If they get it wrong 3 times, print `Account locked`.

**Test it twice:**

| You type | Expected output |
|---|---|
| `abc`, then `python123` | `Access granted` (after 2 tries) |
| `abc`, `123`, `pass` | `Account locked` |
# C2
---
# Mini-project · 80 min

Open **`template.py`** (in this `LAB` folder). It has the structure already — you fill in the marked sections.

## Choose your lane

Pick **one**. All three are the same program with different words. (You do not have to
keep the lane you picked in Week 1.)

| Lane | Your three inputs | Example |
|---|---|---|
| **AI / Data Science** | dataset name, rows loaded, rows expected | `survey_2026`, `1187`, `1200` |
| **Cyber Security** | source IP, failed logins, total attempts | `10.0.0.5`, `12`, `400` |
| **IT** | hostname, GB used, GB total | `srv-01`, `87`, `120` |

## What to build

**Threshold — pass standard.** Ask for the three values. Decide `OVER LIMIT` or `OK`
using `if` / `else`. Print them back in a bordered report.

```
==================================
  RECORD CHECK  -  srv-01
==================================
  Used        : 87
  Total       : 120
  Status      : OK
==================================
```

**Typical.** As above, and it *calculates* two things it was not given — the difference,
and the value as a percentage of the total. Use `if` / `elif` / `else` for a 3-tier
status: `OVER LIMIT` (100%+), `WARNING` (90%+), otherwise `OK`. All numbers show 2
decimal places and are right-aligned so they line up.

```
==================================
  RECORD CHECK  -  srv-01
==================================
  Used        :      87.00
  Total       :     120.00
  Free        :      33.00
  Percent     :      72.50 %
  Status      :         OK
==================================
```

**Excellent.** Wrap the whole thing in a loop so you can check as many records as you
like in one run — type `quit` as the label to stop. Keep count of how many records came
back `OVER LIMIT` during the session, and print that count once, after the loop ends.

## Rules

- **Do not type any number you could calculate.**
- Convert every value the user gives you to the right type.
- **No lists yet**: that is Week 4.

## When it works

1. Run it three times with different inputs. Does it still look right?
2. Run it with a total of `0`. Note the error, but **do not fix it** yet. That comes later.
---
# Optional revision · not submitted

If you have time, answer these on paper. They are good revision, but they are not checked.

- What does indentation control in Python, and what happens if you get it wrong?
- What is the difference between `=` and `==`?
- Why can a `while` loop run forever, and what stops that happening by accident?
- Which error did you meet most today, and what did it turn out to mean?
---
# Wrap-up · 15 min

## 1. This week's cheat sheet

On the **same sheet of paper** you started in Week 1, add your handwritten notes for this week.
This week's cheat sheet should contain notes about:

1. **Comparisons:** `==`, `!=`, `<`, `>`, `<=`, `>=`, and why `==` is not the same as `=`
2. **Combining conditions:** `and`, `or`, `not`
3. **Decisions:** `if` / `elif` / `else` (Python runs the first branch that is True)
4. **Indentation:** the indented lines are the ones inside the `if` or the loop
5. **`while` loops:** the condition must change; `while True` with `break`; `continue`
6. **`for` loops:** `range(stop)`, `range(start, stop, step)` (stop is not included), and `enumerate()`
7. **`for` or `while`?** `for` when you know how many times, `while` when you don't

Write them in your own words, with a short example for each. Do not copy from the slides.
---
## 2. Add your cheat sheet notes here

Take a clear photo of your **whole** cheat sheet page (Week 1 and Week 2 notes), then click into
this cell and paste it (`Ctrl+V` / `Cmd+V`), or drag the image file in.

*(paste here)*
![IMG_4708 (1).jpg](<attachment:IMG_4708 (1).jpg>)

---
## 3. Push to GitHub

Save this notebook and `template.py`. Then open the `CST1510` folder in VS Code and run these
three commands in its terminal:

```
git add .
git commit -m "Week 2 lab and mini-project"
git push
```

Finally, open your repository on GitHub and check that this week's `LAB` folder is there.
If it is not, type `pwd` in the terminal to check which folder you are in.
