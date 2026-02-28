# Milestone 4.18 Quick Guide: Defining and Calling Python Functions

## What You'll Demonstrate

Show that you can define, call, and reuse Python functions with clear inputs, outputs, and execution flow.

---

## Files for This Milestone

- `src/functions_definition_calling_demo.py` - Standalone functions demo script
- `MILESTONE_4_18_QUICK_GUIDE.md` - This walkthrough guide

---

## What the Script Covers

The script demonstrates all required milestone outcomes:

1. **Defining functions with `def`**
   - Uses clear function names
   - Keeps function bodies focused and readable

2. **Calling functions**
   - Calls functions from `main()`
   - Shows control flow entering and returning from functions

3. **Parameters and arguments**
   - Defines parameters in function signatures
   - Calls functions with different argument values
   - Returns computed results for reuse

4. **Basic function scope**
   - Demonstrates global variable visibility
   - Demonstrates local variables inside a function
   - Explains why local variables should stay self-contained

---

## Run the Script

From project root:

```powershell
python src/functions_definition_calling_demo.py
```

If `python` is not directly available:

```powershell
C:/Users/kisho/OneDrive/Desktop/new12/.venv/Scripts/python.exe src/functions_definition_calling_demo.py
```

---

## Expected Output Highlights

You should see:

- A function definition being called successfully
- Multiple function calls with different argument values
- Return values printed and reused
- A simple execution-flow sequence (start, calls, return)
- Local vs global scope behavior explained through printed output

---

## Why This Matters

Functions improve code quality by helping you:

- Avoid repetition
- Keep scripts modular and readable
- Reuse logic safely
- Debug smaller blocks of code
- Scale programs more easily

Functions are core building blocks of maintainable Python programs.

---

## Video Recording Checklist (~2 Minutes)

### Part 1: Define + Call a Function (35 sec)
- [ ] Open `src/functions_definition_calling_demo.py`
- [ ] Show at least one function defined with `def`
- [ ] Call that function and show output

### Part 2: Parameters and Arguments (35 sec)
- [ ] Show function signature with parameters
- [ ] Call same function with different arguments
- [ ] Explain how arguments change output

### Part 3: Execution Flow (30 sec)
- [ ] Run script in terminal
- [ ] Explain order: `main()` -> called function -> return to caller
- [ ] Point out returned values

### Part 4: Basic Scope (20 sec)
- [ ] Show global variable usage
- [ ] Show local variable inside a function
- [ ] Explain local variable lifetime and isolation

---

## Suggested 2-Minute Script

"In this milestone, I’m demonstrating Python functions using `src/functions_definition_calling_demo.py`.

First, I define functions with `def` and call them from `main()`.

Second, I show parameters and arguments by calling the same function with different values, which produces different outputs.

Third, I demonstrate execution flow: the program enters a function, runs its logic, returns a result, and continues in the caller.

Finally, I show basic scope: global variables can be read in functions, while local variables exist only inside the function that defines them.

This makes code more reusable, readable, and maintainable." 

---

## Submission Checklist

- [ ] Script created in `src/`
- [ ] Script runs successfully in terminal
- [ ] At least one function defined using `def`
- [ ] Function called from code
- [ ] Parameters and arguments demonstrated
- [ ] Execution flow explained clearly
- [ ] Local vs global scope demonstrated at a basic level
- [ ] ~2 minute screen video recorded and link ready
