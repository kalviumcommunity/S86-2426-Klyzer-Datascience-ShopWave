# Milestone 4.19 Quick Guide: Passing Data into Functions and Returning Results

## What You'll Demonstrate

Show that you can design Python functions as clear input-output units by passing arguments in and returning values out.

---

## Files for This Milestone

- `src/functions_input_output_demo.py` - Standalone input/output functions demo
- `MILESTONE_4_19_QUICK_GUIDE.md` - This walkthrough guide

---

## What the Script Covers

The script demonstrates all required milestone concepts:

1. **Parameters and arguments**
   - Defines functions with meaningful parameters
   - Calls the same function with different arguments

2. **Returning values**
   - Uses `return` for computed results
   - Avoids print-only function design for core logic

3. **Using returned results**
   - Stores outputs in variables
   - Reuses returned values in additional calculations
   - Passes returned values to other functions

4. **Avoiding common mistakes**
   - Avoids hardcoded values in reusable logic
   - Separates calculation (`return`) from display (`print` in `main`)
   - Handles edge cases with predictable return values

---

## Run the Script

From project root:

```powershell
python src/functions_input_output_demo.py
```

If `python` is not directly available:

```powershell
C:/Users/kisho/OneDrive/Desktop/new12/.venv/Scripts/python.exe src/functions_input_output_demo.py
```

---

## Expected Output Highlights

You should see:

- Revenue values computed from different function arguments
- A discounted total returned and reused
- Tax and final total calculated from returned values
- Average order value computed from returned totals
- A safe edge-case return (`None`) for divide-by-zero input

---

## Why This Matters

When functions return values cleanly:

- Logic is modular and reusable
- Data flow is easier to trace and test
- Programs are easier to maintain
- Side effects are reduced

Good function design improves clarity and long-term scalability.

---

## Video Recording Checklist (~2 Minutes)

### Part 1: Parameters and Arguments (35 sec)
- [ ] Open `src/functions_input_output_demo.py`
- [ ] Show a function signature with parameters
- [ ] Call it with different argument values

### Part 2: Returning Values (30 sec)
- [ ] Show `return` statements in calculation functions
- [ ] Explain why return is preferred over print-only logic

### Part 3: Reusing Returned Results (35 sec)
- [ ] Run script in terminal
- [ ] Show returned values stored in variables
- [ ] Show returned result passed into another function

### Part 4: Common Mistakes and Edge Case (20 sec)
- [ ] Explain avoiding hardcoded values
- [ ] Show safe edge case handling (`None` return)
- [ ] Summarize input-output function behavior

---

## Suggested 2-Minute Script

"In this milestone, I’m demonstrating how data flows into and out of Python functions using `src/functions_input_output_demo.py`.

First, I define functions with parameters and call them with different arguments.

Second, I show calculation functions that use `return` to send values back, instead of only printing inside the function.

Third, I store returned values in variables, reuse them in further calculations, and pass results to other functions.

Finally, I show a safe edge case where a function returns `None` for invalid input, which keeps the behavior predictable.

This input-output pattern makes code reusable, testable, and easier to maintain." 

---

## Submission Checklist

- [ ] Script created in `src/`
- [ ] Script runs successfully in terminal
- [ ] Function parameters defined clearly
- [ ] Arguments passed correctly in calls
- [ ] Values returned using `return`
- [ ] Returned results stored and reused
- [ ] Edge-case behavior handled predictably
- [ ] ~2 minute screen video recorded and link ready
