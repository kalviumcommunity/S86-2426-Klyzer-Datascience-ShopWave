# Milestone 4.16 Quick Guide: Writing Conditional Statements for Data Logic

## What You'll Demonstrate

Show that you can use Python conditional logic to control program flow using clear, correct, and readable decision blocks.

---

## Files for This Milestone

- `src/conditional_statements_demo.py` - Standalone conditional logic demo script
- `MILESTONE_4_16_QUICK_GUIDE.md` - This walkthrough guide

---

## What the Script Covers

The script demonstrates all required concepts with focused examples:

1. **Basic `if` statement**
   - Checks a single condition
   - Executes only when condition is true

2. **`if-else` branching**
   - Handles both true and false outcomes
   - Keeps branching clear and predictable

3. **`if-elif-else` for multiple conditions**
   - Evaluates multiple paths in order
   - Ensures one decision path is selected

4. **Numeric and string comparisons**
   - Uses both number-based and text-based checks
   - Demonstrates practical data-driven decisions

5. **Logical operators**
   - `and` for combined required conditions
   - `or` for alternative matching conditions
   - `not` for inversion checks

6. **Edge-case boundary check**
   - Demonstrates intentional handling of threshold values

---

## Run the Script

From project root:

```powershell
python src/conditional_statements_demo.py
```

If `python` is not directly available:

```powershell
C:/Users/kisho/OneDrive/Desktop/new35/.venv/Scripts/python.exe src/conditional_statements_demo.py
```

---

## Expected Output Highlights

You should see:

- A true-path `if` example
- A clear `if-else` in-stock/out-of-stock decision
- A multi-branch `if-elif-else` quality classification
- Numeric and string comparison outcomes
- `and`, `or`, and `not` logic outputs
- A boundary-value edge-case check

---

## Why This Matters

Strong conditional logic helps you:

- Prevent incorrect decision behavior
- Make workflows deterministic and testable
- Handle edge cases intentionally
- Keep business/data logic readable and maintainable

Conditionals are the foundation of intelligent Python workflows.

---

## Video Recording Checklist (~2 Minutes)

### Part 1: Basic if and if-else (35 sec)
- [ ] Open `src/conditional_statements_demo.py`
- [ ] Show the simple `if` example and explain true-only execution
- [ ] Show `if-else` and explain both branches

### Part 2: if-elif-else (30 sec)
- [ ] Show ordered multi-condition checks
- [ ] Explain why order matters
- [ ] Run and point out selected branch

### Part 3: Logical Operators (35 sec)
- [ ] Show `and`, `or`, and `not` conditions
- [ ] Explain outcome for each condition
- [ ] Emphasize readability in combined conditions

### Part 4: Decision Outcomes + Edge Case (20 sec)
- [ ] Point to printed outcomes for each section
- [ ] Show threshold boundary check
- [ ] Summarize how conditionals control flow safely

---

## Suggested 2-Minute Script

"In this milestone, I’m demonstrating conditional logic in Python using `src/conditional_statements_demo.py`.

First, I show a basic `if` statement where code runs only when a condition is true.

Second, I use `if-else` to handle both outcomes, which makes logic predictable.

Third, I use `if-elif-else` to classify a score across multiple ranges, and I explain why condition order matters.

Then I demonstrate numeric and string conditions, followed by logical operators: `and`, `or`, and `not`.

Finally, I show a boundary-value example to highlight edge-case handling. Together, these patterns make data logic clear, safe, and maintainable." 

---

## Submission Checklist

- [ ] Script created in `src/`
- [ ] Script runs successfully in terminal
- [ ] Basic `if` demonstrated
- [ ] `if-else` demonstrated
- [ ] `if-elif-else` demonstrated
- [ ] Logical operators (`and`, `or`, `not`) demonstrated
- [ ] Decision outcomes explained clearly
- [ ] ~2 minute screen video recorded and link ready
