# Milestone 4.14 Quick Guide: Understanding Python Numeric and String Data Types

## What You'll Demonstrate

Show that you understand Python numeric and string types, can perform basic operations, and can handle type mismatches safely.

---

## Files for This Milestone

- `src/numeric_string_types_demo.py` - Standalone Python demo script
- `MILESTONE_4_14_QUICK_GUIDE.md` - This walkthrough guide

---

## What the Script Covers

The script demonstrates the exact fundamentals required in this milestone:

1. **Numeric data types**
   - Integer (`int`) and floating-point (`float`) variables
   - Arithmetic operations: `+`, `-`, `*`, `/`, `//`
   - Basic precision example: `0.1 + 0.2`

2. **String data types**
   - Creating strings
   - Concatenating text
   - Accessing characters and slices

3. **Mixing numbers and strings safely**
   - Shows a real `TypeError` when concatenating `str + int`
   - Fixes using `str()` conversion
   - Converts numeric text to number using `int()`

4. **Inspecting types**
   - Uses `type()` to inspect values at runtime
   - Reinforces debugging habits

---

## Run the Script

From project root:

```powershell
python src/numeric_string_types_demo.py
```

If `python` is not available directly:

```powershell
C:/Users/kisho/OneDrive/Desktop/new35/.venv/Scripts/python.exe src/numeric_string_types_demo.py
```

---

## Expected Output Highlights

You should see:

- `int` and `float` values with arithmetic results
- String concatenation and string indexing/slicing examples
- A controlled `TypeError` message for mixed types
- Corrected output after explicit conversion
- Type inspection output for multiple values

---

## Why This Matters

Understanding data types prevents common beginner bugs:

- Wrong calculations because numbers are stored as text
- Runtime errors from mixing incompatible types
- Confusing output formatting
- Hard-to-debug logic issues

Strong type awareness makes code safer, clearer, and easier to debug.

---

## Video Recording Checklist (~2 Minutes)

### Part 1: Show Numeric Examples (30 sec)
- [ ] Open `src/numeric_string_types_demo.py`
- [ ] Point out `whole_number` and `decimal_number`
- [ ] Explain arithmetic operations and division difference (`/` vs `//`)
- [ ] Mention precision example `0.1 + 0.2`

### Part 2: Show String Examples (25 sec)
- [ ] Show string variables and concatenation
- [ ] Show string indexing and slicing output
- [ ] Explain strings are text, not numbers

### Part 3: Show Mixed-Type Handling (35 sec)
- [ ] Run script in terminal
- [ ] Point to displayed `TypeError`
- [ ] Explain why `"text" + number` fails
- [ ] Show fix using `str()` and conversion using `int()`

### Part 4: Show Type Inspection + Why It Matters (20 sec)
- [ ] Point out `type()` output
- [ ] Explain checking types helps debugging
- [ ] Summarize: "Numbers and text must be handled intentionally"

---

## Suggested 2-Minute Script

"In this milestone, I’m demonstrating Python numeric and string data types using a standalone script in `src/numeric_string_types_demo.py`.

First, numeric types: I use an integer and a float, then perform arithmetic operations including true division and floor division. I also show a basic precision example with `0.1 + 0.2`.

Next, string types: I create text variables, concatenate them, and access string values using indexing and slicing.

Then I demonstrate a common error when mixing text and numbers directly. The script shows a TypeError and then fixes it using explicit conversion with `str()`. I also convert numeric text into an integer with `int()`.

Finally, I use `type()` to inspect values during execution. This habit helps detect mismatches early and keeps code reliable." 

---

## Submission Checklist

- [ ] Script created and saved in `src/`
- [ ] Script runs successfully in terminal
- [ ] Numeric examples explained (`int`, `float`, arithmetic)
- [ ] String examples explained (concatenation, access)
- [ ] Mixed-type issue and fix demonstrated
- [ ] Type inspection shown with `type()`
- [ ] ~2 minute screen video recorded and link ready
