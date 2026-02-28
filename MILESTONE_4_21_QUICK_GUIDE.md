# Milestone 4.21 Quick Guide: Structuring Python Code for Readability and Reuse

## What You'll Demonstrate

Show that you can organize Python code into clear sections, reduce repetition with functions, and keep execution flow easy to follow.

---

## Files for This Milestone

- `src/code_structure_readability_reuse_demo.py` - Standalone structure and reuse demo script
- `MILESTONE_4_21_QUICK_GUIDE.md` - This walkthrough guide

---

## What the Script Covers

The script demonstrates all required milestone outcomes:

1. **Organizing code into logical sections**
   - Imports and constants at the top
   - Reusable helper functions in the middle
   - Clean execution block (`main`) at the bottom

2. **Using functions for reuse**
   - Repeated order summary logic is extracted into helper functions
   - Reuse is shown by calling the same function for multiple orders

3. **Separating logic from execution**
   - Business logic stays in helper functions
   - Top-level execution is minimal and readable

4. **Readable and maintainable structure**
   - Clear naming and spacing
   - No deeply nested logic
   - Predictable top-to-bottom flow

---

## Run the Script

From project root:

```powershell
python src/code_structure_readability_reuse_demo.py
```

If `python` is not directly available:

```powershell
C:/Users/kisho/OneDrive/Desktop/new12/.venv/Scripts/python.exe src/code_structure_readability_reuse_demo.py
```

---

## Expected Output Highlights

You should see:

- A section describing script layout
- Two order summaries produced from the same reusable function
- Calculated subtotal, tax, and final total for each order
- A final section explaining why structure improves maintainability

---

## Why This Matters

Good structure helps you:

- Navigate code quickly
- Reuse logic instead of duplicating code
- Debug and modify scripts safely
- Scale projects with less confusion

Structured code is easier for both you and teammates to maintain.

---

## Video Recording Checklist (~2 Minutes)

### Part 1: Script Structure Overview (35 sec)
- [ ] Open `src/code_structure_readability_reuse_demo.py`
- [ ] Point out imports/constants section
- [ ] Point out helper functions section
- [ ] Point out `main()` execution section

### Part 2: Reuse Through Functions (35 sec)
- [ ] Show repeated logic extracted into `summarize_order`
- [ ] Show function called for two different orders
- [ ] Explain why this avoids duplication

### Part 3: Logic vs Execution Separation (30 sec)
- [ ] Show calculations inside helper functions
- [ ] Show clean top-level flow inside `main()`
- [ ] Explain readability benefit

### Part 4: Why Structure Matters (20 sec)
- [ ] Run script and show output sections
- [ ] Summarize maintainability and collaboration benefits

---

## Suggested 2-Minute Script

"In this milestone, I’m demonstrating how to structure Python code for readability and reuse using `src/code_structure_readability_reuse_demo.py`.

The script is organized into three clear sections: imports and constants, helper functions, and a clean `main()` execution block.

I use helper functions to calculate subtotal, tax, and final totals, then reuse the same summary function for different orders.

This avoids duplicate logic and makes updates safer, because the core calculations are centralized.

Overall, the structure reads from top to bottom like a story and is easier to understand, debug, and extend." 

---

## Submission Checklist

- [ ] Script created in `src/`
- [ ] Script runs successfully in terminal
- [ ] Code organized into logical sections
- [ ] Repeated logic extracted into reusable functions
- [ ] Top-level execution kept clean in `main()`
- [ ] Readability and maintainability benefits explained
- [ ] ~2 minute screen video recorded and link ready
