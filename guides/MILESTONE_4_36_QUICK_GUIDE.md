# Milestone 4.36: Standardizing Column Names and Data Formats - Quick Guide

## 2-Minute Demonstration Video Script

**Total Duration:** 2 minutes (120 seconds)

---

## Section 1: Introduction (0:00 - 0:15) - 15 seconds

**Script:**

> "Welcome! This is Milestone 4.36—Standardizing Column Names and Data Formats. Today you'll learn why messy column names break your code and how to fix them with snake_case and text standardization. Let's get started!"

**What to show:**
- Title slide: "Milestone 4.36: Standardizing Column Names and Data Formats"
- Your face/screen with the notebook open

**Key point:** Set expectations—standardization makes code cleaner and more reliable

---

## Section 2: The Problem - Messy Column Names (0:15 - 0:30) - 15 seconds

**Script:**

> "First, the problem. Load employee data and look at these column names: 'First Name', 'LAST_NAME', 'Salary ($)'. Mixed casing, spaces, and special characters. This makes code messy and error-prone. Watch what happens when we try normal access."

**What to show:**
```python
# Run this cell
employees_df = pd.read_csv('../data/raw/employee_records.csv')
print("Column names:")
print(employees_df.columns.tolist())
```

**Expected output:**
```
Column names:
['Employee ID', 'First Name', 'LAST_NAME', 'Email Address', 
 'Department Name', 'Salary ($)', 'Hire Date', 'Status']
```

**What to demonstrate:**
- Point out mixed casing: "First Name" vs "LAST_NAME"
- Point out spaces: "Email Address"
- Point out special characters: "Salary ($)"

**Narration emphasis:**
> "See? 'First Name', 'LAST_NAME', 'Salary ($)'—totally inconsistent!"

---

## Section 3: Solution - Standardize Column Names (0:30 - 0:50) - 20 seconds

**Script:**

> "Now the solution! I'll create a function that converts everything to lowercase, replaces spaces with underscores, and removes special characters. This is called snake_case—the professional standard. Let's apply it."

**What to show:**
```python
# Run this cell
def standardize_column_names(df):
    df_clean = df.copy()
    df_clean.columns = (df_clean.columns
                        .str.lower()
                        .str.replace(' ', '_', regex=False)
                        .str.replace(r'[^a-z0-9_]', '', regex=True)
                        .str.replace(r'_+', '_', regex=True)
                        .str.strip('_'))
    return df_clean

employees_clean = standardize_column_names(employees_df)
print("Standardized columns:")
print(employees_clean.columns.tolist())
```

**Expected output:**
```
Standardized columns:
['employee_id', 'first_name', 'last_name', 'email_address',
 'department_name', 'salary', 'hire_date', 'status']
```

**What to demonstrate:**
- Show function creation (briefly)
- Show before/after column names
- Emphasize snake_case: all lowercase with underscores

**Narration emphasis:**
> "Now every column is lowercase with underscores—clean and consistent!"

---

## Section 4: Standardizing Text Data (0:50 - 1:15) - 25 seconds

**Script:**

> "Next, text data. Look at the Department column—'Sales', 'sales', 'SALES'. Same department, but treated as different values. Let's fix it by stripping whitespace and standardizing case to Title Case."

**What to show:**
```python
# Run this cell - Show problem
print("Department (BEFORE):")
print(employees_clean.department_name.unique())
print(f"Unique values: {employees_clean.department_name.nunique()}")

# Strip whitespace and title case
employees_clean['department_name'] = employees_clean['department_name'].str.strip().str.title()
employees_clean['status'] = employees_clean['status'].str.strip().str.title()

print("\nDepartment (AFTER):")
print(employees_clean.department_name.unique())
print(f"Unique values: {employees_clean.department_name.nunique()}")
```

**Expected output:**
```
Department (BEFORE):
['  Sales  ' 'MARKETING' 'sales' 'IT' 'it']
Unique values: 5

Department (AFTER):
['Sales' 'Marketing' 'It']
Unique values: 3
```

**What to demonstrate:**
- Show multiple variations of "Sales" (with spaces, different casing)
- Apply `.str.strip()` and `.str.title()`
- Show unified values after standardization

**Narration emphasis:**
> "Before: 5 variations. After: 3 clean values. Now grouping works correctly!"

---

## Section 5: Standardizing Numeric Data (1:15 - 1:35) - 20 seconds

**Script:**

> "Next, salary. It's stored as text because of dollar signs. Can't calculate averages! Remove the symbols, convert to float, and boom—math works."

**What to show:**
```python
# Run this cell - Show problem
print("Salary data type:", employees_clean.salary.dtype)
print("Sample:", employees_clean.salary.head(3))

# Try to calculate mean (show it won't work)
try:
    print("Mean:", employees_clean.salary.mean())
except:
    print("❌ ERROR: Cannot calculate mean!")

# Fix it
employees_clean['salary'] = (employees_clean['salary']
                             .str.replace('$', '', regex=False)
                             .str.replace(',', '', regex=False)
                             .astype(float))

print("\nAfter standardization:")
print("Data type:", employees_clean.salary.dtype)
print(f"Mean salary: ${employees_clean.salary.mean():,.2f}")
```

**Expected output:**
```
Salary data type: object
Sample: 0    75000
        1    82000
        ...
❌ ERROR: Cannot calculate mean!

After standardization:
Data type: float64
Mean salary: $75,200.00
```

**What to demonstrate:**
- Show salary is "object" (text) type
- Show error when trying to calculate mean
- Remove "$" and convert to float
- Show successful mean calculation

**Narration emphasis:**
> "Now salary is numeric—calculations work perfectly!"

---

## Section 6: Before and After Comparison (1:35 - 1:55) - 20 seconds

**Script:**

> "Let's compare. Before: messy names, mixed casing, text where numbers should be. After: clean snake_case, standardized text, proper data types. This is professional data preparation!"

**What to show:**
```python
# Run this cell
print("=" * 70)
print("BEFORE vs AFTER")
print("=" * 70)
print("\nColumn Names:")
for old, new in zip(employees_df.columns[:4], employees_clean.columns[:4]):
    print(f"  {old:25} → {new}")

print("\nData Quality:")
print(f"  Department unique values: {employees_df['Department Name'].nunique()} → {employees_clean.department_name.nunique()}")
print(f"  Salary data type: {employees_df['Salary ($)'].dtype} → {employees_clean.salary.dtype}")
print(f"  Mean salary possible: No → Yes (${employees_clean.salary.mean():,.2f})")
```

**Expected output:**
```
======================================================================
BEFORE vs AFTER
======================================================================

Column Names:
  Employee ID              → employee_id
  First Name               → first_name
  LAST_NAME                → last_name
  Email Address            → email_address

Data Quality:
  Department unique values: 5 → 3
  Salary data type: object → float64
  Mean salary possible: No → Yes ($75,200.00)
```

**What to demonstrate:**
- Side-by-side column name comparison
- Show improvement in data quality metrics
- Emphasize numeric operations now work

**Narration emphasis:**
> "Clean names, consistent text, proper types—ready for analysis!"

---

## Section 7: Wrap-Up and Key Takeaways (1:55 - 2:00) - 5 seconds

**Script:**

> "Remember: Always standardize at the start. Use snake_case for columns. Clean text with strip and title. Convert types properly. You're ready to create professional, analysis-ready datasets!"

**What to show:**
- Final cleaned DataFrame: `employees_clean.head()`
- Smile and wave

**Key message:** Standardization is a critical first step in every data workflow

---

## Success Criteria Checklist

Your video MUST demonstrate these 5 things clearly:

### ✅ Required Demonstrations:

1. **Show messy column names**
   - Display original columns with spaces, mixed case, special characters
   - Explain why this is a problem

2. **Apply column name standardization**
   - Show function that converts to snake_case
   - Display before/after column names
   - Demonstrate clean access: `df.column_name`

3. **Standardize text data**
   - Show inconsistent text (mixed case, extra whitespace)
   - Apply `.str.strip()` and `.str.title()` (or `.str.lower()`)
   - Show unified category values

4. **Standardize at least one numeric or date format**
   - Show salary as text (object type)
   - Remove currency symbols and convert to numeric
   - Demonstrate calculations now work (mean, sum, etc.)

5. **Show before/after comparison**
   - Side-by-side comparison of column names
   - Show data quality improvements (fewer unique values, correct types)
   - Emphasize professional result

---

## Code Blocks to Run (In Order)

### Block 1: Load and Show Problem (0:15 - 0:30)
```python
import pandas as pd

employees_df = pd.read_csv('../data/raw/employee_records.csv')
print("Column names:")
print(employees_df.columns.tolist())
print("\nSample data:")
print(employees_df.head(3))
```

### Block 2: Standardize Column Names (0:30 - 0:50)
```python
def standardize_column_names(df):
    df_clean = df.copy()
    df_clean.columns = (df_clean.columns
                        .str.lower()
                        .str.replace(' ', '_', regex=False)
                        .str.replace(r'[^a-z0-9_]', '', regex=True)
                        .str.replace(r'_+', '_', regex=True)
                        .str.strip('_'))
    return df_clean

employees_clean = standardize_column_names(employees_df)
print("Standardized columns:")
print(employees_clean.columns.tolist())
```

### Block 3: Standardize Text Data (0:50 - 1:15)
```python
print("Department (BEFORE):")
print(employees_clean.department_name.unique())
print(f"Unique values: {employees_clean.department_name.nunique()}")

# Standardize
employees_clean['department_name'] = employees_clean['department_name'].str.strip().str.title()
employees_clean['status'] = employees_clean['status'].str.strip().str.title()

print("\nDepartment (AFTER):")
print(employees_clean.department_name.unique())
print(f"Unique values: {employees_clean.department_name.nunique()}")

print("\nStatus (AFTER):")
print(employees_clean.status.unique())
```

### Block 4: Standardize Numeric Data (1:15 - 1:35)
```python
print("Salary (BEFORE):")
print(f"  Type: {employees_clean.salary.dtype}")
print(f"  Sample: {employees_clean.salary.head(2).tolist()}")

try:
    mean_salary = employees_clean.salary.mean()
    print(f"  Mean: {mean_salary}")
except:
    print("  ❌ ERROR: Cannot calculate mean!")

# Fix it
employees_clean['salary'] = (employees_clean['salary']
                             .str.replace('$', '', regex=False)
                             .str.replace(',', '', regex=False)
                             .astype(float))

print("\nSalary (AFTER):")
print(f"  Type: {employees_clean.salary.dtype}")
print(f"  Mean: ${employees_clean.salary.mean():,.2f}")
print(f"  Max: ${employees_clean.salary.max():,.2f}")
```

### Block 5: Before/After Comparison (1:35 - 1:55)
```python
print("=" * 70)
print("BEFORE vs AFTER COMPARISON")
print("=" * 70)

print("\n📋 Column Names:")
for old, new in zip(employees_df.columns, employees_clean.columns):
    print(f"  {old:30} → {new}")

print("\n📊 Data Quality Improvements:")
print(f"  Department variations: {employees_df['Department Name'].nunique()} → {employees_clean.department_name.nunique()}")
print(f"  Salary type: {employees_df['Salary ($)'].dtype} → {employees_clean.salary.dtype}")
print(f"  Mean calculation: Not possible → ${employees_clean.salary.mean():,.2f}")

print("\n✅ Result: Professional, analysis-ready data!")
```

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Not showing the problem first
**Fix:** Always show messy data BEFORE cleaning to demonstrate the need

### ❌ Mistake 2: Forgetting to show before/after comparison
**Fix:** Use print statements to clearly show transformations

### ❌ Mistake 3: Not explaining snake_case
**Fix:** Explicitly state: "snake_case means all lowercase with underscores"

### ❌ Mistake 4: Skipping text standardization
**Fix:** Must demonstrate `.str.strip()` and `.str.title()` or `.str.lower()`

### ❌ Mistake 5: Not verifying numeric conversion
**Fix:** Show calculation (mean, sum) works after converting to numeric

---

## Tips for a Great Video

### Speaking Tips:
- Speak clearly and at a steady pace
- Don't rush—2 minutes is enough time
- Emphasize key terms: "snake_case", "standardize", "consistent"
- Show enthusiasm—this is a critical skill!

### Visual Tips:
- Make sure code output is clearly visible
- Use zoom if needed for readability
- Point to specific parts of output with cursor
- Keep your face visible (if using webcam)

### Technical Tips:
- Test all code blocks before recording
- Have notebook open and cells cleared
- Run cells one at a time
- Don't worry about minor mistakes—keep going!

### Timing Tips:
- Practice once before recording
- Use a timer to stay on track
- If you go 5-10 seconds over, that's okay
- Better to be clear than to rush

---

## Troubleshooting Guide

### Issue: Column names don't change
**Cause:** Forgot to assign result back to DataFrame
**Fix:** `df.columns = ...` or `df = standardize_column_names(df)`

### Issue: Salary conversion fails
**Cause:** Some values may have unexpected characters
**Fix:** Add more `.str.replace()` calls to remove all non-numeric characters

### Issue: Text standardization doesn't unify values
**Cause:** Extra whitespace not removed
**Fix:** Always call `.str.strip()` BEFORE `.str.title()` or `.str.lower()`

### Issue: Date conversion fails
**Cause:** Too many mixed formats
**Fix:** Use `pd.to_datetime(df['col'], infer_datetime_format=True, errors='coerce')`

### Issue: Function doesn't work on your data
**Cause:** Your data has different column names
**Fix:** Adjust the column list in function parameters

---

## After Recording Checklist

✅ Video is between 1:50 and 2:10 in length

✅ Showed messy column names with spaces and special characters

✅ Demonstrated snake_case standardization function

✅ Showed text cleaning (strip and title/lower case)

✅ Converted at least one column to proper numeric type

✅ Displayed before/after comparison

✅ Explained why standardization matters

✅ Code executed without errors

✅ Audio is clear and understandable

✅ Screen is readable (code and output visible)

---

## Key Concepts to Emphasize

### 1. snake_case Convention
- All lowercase letters
- Underscores instead of spaces
- No special characters
- Industry standard for Python/Pandas

### 2. Text Standardization
- `.str.strip()` removes leading/trailing whitespace
- `.str.title()` converts to Title Case (or `.str.lower()` for lowercase)
- Ensures consistent category values

### 3. Type Conversion
- Remove symbols ($ , etc.) before converting to numeric
- Use `.astype(float)` or `.astype(int)`
- Verify with `.dtype` after conversion

### 4. Why Standardization Matters
- **For code:** Clean column access, no quotes needed
- **For data:** Correct grouping, accurate statistics
- **For workflow:** Easier merging, reusable code
- **For team:** Consistent standards, readable code

---

## Example Narration (Full Script)

> [0:00] "Welcome! This is Milestone 4.36—Standardizing Column Names and Data Formats. Today you'll learn why messy column names break your code and how to fix them with snake_case and text standardization. Let's get started!"
>
> [0:15] "First, the problem. Load employee data and look at these column names: 'First Name', 'LAST_NAME', 'Salary ($)'. Mixed casing, spaces, and special characters. This makes code messy and error-prone."
>
> [0:30] "Now the solution! I'll create a function that converts everything to lowercase, replaces spaces with underscores, and removes special characters. This is called snake_case—the professional standard. Let's apply it... Perfect! Now every column is lowercase with underscores."
>
> [0:50] "Next, text data. Look at the Department column—'Sales', 'sales', 'SALES'. Same department, but treated as different values. Let's fix it by stripping whitespace and standardizing case to Title Case... Before: 5 variations. After: 3 clean values. Now grouping works correctly!"
>
> [1:15] "Next, salary. It's stored as text because of dollar signs. Can't calculate averages! Remove the symbols, convert to float, and boom—math works. Now salary is numeric—calculations work perfectly!"
>
> [1:35] "Let's compare. Before: messy names, mixed casing, text where numbers should be. After: clean snake_case, standardized text, proper data types. This is professional data preparation!"
>
> [1:55] "Remember: Always standardize at the start. Use snake_case for columns. Clean text with strip and title. Convert types properly. You're ready to create professional, analysis-ready datasets!"

---

## Final Notes

**Remember:** This video demonstrates a CRITICAL skill that applies to EVERY data analysis project.

**Professional workflow:**
1. Load data
2. Standardize column names immediately
3. Standardize text and numeric formats
4. Verify data types
5. Proceed with analysis

**This habit will:**
- Make your code cleaner
- Reduce errors
- Speed up development
- Impress employers and colleagues

**Good luck with your recording!** 🎥🚀
