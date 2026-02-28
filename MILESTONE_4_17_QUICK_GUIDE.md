# Milestone 4.17 Quick Guide: Using for and while Loops for Iterative Data Processing

## What You'll Demonstrate

Show that you can use Python loops to process repeated logic safely, clearly, and predictably.

---

## Files for This Milestone

- `src/loops_iterative_processing_demo.py` - Standalone loops demo script
- `MILESTONE_4_17_QUICK_GUIDE.md` - This walkthrough guide

---

## What the Script Covers

The script demonstrates all milestone requirements with focused examples:

1. **`for` loops for known sequences**
   - Iterates through a numeric range
   - Iterates through a list of values
   - Uses loop variables meaningfully

2. **`while` loop for condition-based repetition**
   - Repeats while a condition is true
   - Updates the condition variable correctly
   - Terminates intentionally

3. **Loop control with `break` and `continue`**
   - Uses `continue` to skip selected iterations
   - Uses `break` to exit early when a condition is met

4. **Avoiding infinite loops**
   - Shows a common unsafe pattern
   - Demonstrates safe variable updates for termination

---

## Run the Script

From project root:

```powershell
python src/loops_iterative_processing_demo.py
```

If `python` is not directly available:

```powershell
C:/Users/kisho/OneDrive/Desktop/new12/.venv/Scripts/python.exe src/loops_iterative_processing_demo.py
```

---

## Expected Output Highlights

You should see:

- A `for` loop running over `range(1, 6)` with running totals
- A `for` loop processing each list item in order
- A `while` loop counting down and stopping when condition turns false
- `continue` skipping selected iterations
- `break` stopping a loop early
- A safe loop termination example preventing infinite repetition

---

## Why This Matters

Strong loop logic helps you:

- Remove repetitive code
- Process collections efficiently
- Keep iteration behavior predictable
- Prevent infinite loop bugs
- Build scalable, maintainable workflows

Loops are core automation tools in Python data workflows.

---

## Video Recording Checklist (~2 Minutes)

### Part 1: for Loop Examples (35 sec)
- [ ] Open `src/loops_iterative_processing_demo.py`
- [ ] Show range-based `for` loop
- [ ] Show list-based `for` loop
- [ ] Explain loop execution order briefly

### Part 2: while Loop Example (30 sec)
- [ ] Show condition-controlled `while` loop
- [ ] Explain variable update (`remaining_attempts -= 1`)
- [ ] Show loop ending when condition becomes false

### Part 3: break and continue (35 sec)
- [ ] Show `continue` skipping even values
- [ ] Show `break` stopping at first threshold match
- [ ] Explain why these improve control and readability

### Part 4: Infinite Loop Prevention (20 sec)
- [ ] Point out unsafe pattern with missing variable update
- [ ] Show safe pattern that updates condition variable
- [ ] Summarize: loops must always have clear termination logic

---

## Suggested 2-Minute Script

"In this milestone, I’m demonstrating Python loops in `src/loops_iterative_processing_demo.py`.

First, I show `for` loops: one over a range and one over a list. This is useful when iterating over known sequences.

Second, I show a `while` loop that repeats based on a condition. I update the loop variable each iteration so the loop terminates correctly.

Third, I demonstrate loop control statements: `continue` to skip specific iterations, and `break` to stop a loop early when a condition is met.

Finally, I explain an infinite-loop pitfall and show the safe pattern where the condition variable is updated. This ensures loop behavior is predictable and safe." 

---

## Submission Checklist

- [ ] Script created in `src/`
- [ ] Script runs successfully in terminal
- [ ] `for` loop examples demonstrated
- [ ] `while` loop example demonstrated
- [ ] `break` and/or `continue` demonstrated
- [ ] Infinite loop prevention explained
- [ ] Loop behavior and flow explained clearly
- [ ] ~2 minute screen video recorded and link ready
