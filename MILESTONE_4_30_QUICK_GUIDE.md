# Milestone 4.30: Inspecting DataFrames Using head(), info(), and describe()
## 2-Minute Video Demonstration Guide

---

## Video Requirements

**Duration:** ~2 minutes  
**Format:** Screen capture with visible code execution  
**Audience:** Data Science learners  
**Goal:** Demonstrate the three essential DataFrame inspection methods

---

## 2-Minute Script with Timing

### **Introduction (0:00 - 0:10)** - 10 seconds

**SAY:**
> "Hi! Today I'm demonstrating the three essential DataFrame inspection methods: head(), info(), and describe(). These three methods are mandatory after loading any data—they tell you what your data looks like, its structure, and its statistical properties. Let's inspect a real dataset."

**SHOW:**
- Your notebook open with title visible
- Data already loaded (employees or sales dataset)

---

### **Section 1: Using head() for Visual Preview (0:10 - 0:40)** - 30 seconds

**SAY:**
> "First, head() shows the first few rows of the DataFrame. This gives a quick visual confirmation that data loaded correctly."

**DO:**
```python
import pandas as pd

# Load data
employees_df = pd.read_csv('../data/raw/employees.csv')

# Preview first 5 rows
print("First 5 rows:")
print(employees_df.head())
```

**SAY:**
> "Notice the column names at the top—EmployeeID, Name, Department, Salary, YearsExperience, City. The index is on the left: zero, one, two, three, four. I can see actual data values, which gives me a feel for the dataset. If I need more rows, I can specify: head(10) for ten rows."

**DO (optional):**
```python
print(employees_df.head(3))  # First 3 rows
```

**SHOW:**
- Clear output showing rows and columns
- Point out column names
- Point out index on the left
- Highlight sample values

---

### **Section 2: Using info() for Structure (0:40 - 1:15)** - 35 seconds

**SAY:**
> "Next, info() is the MOST important inspection method. It shows the complete structure: data types, null counts, and memory usage."

**DO:**
```python
print("DataFrame structure:")
employees_df.info()
```

**SAY:**
> "Looking at the output: we have 10 rows and 6 columns. Each column shows its data type—int64 for numbers like EmployeeID and Salary, object for text like Name and Department. The critical part: non-null count. All columns show 10 non-null, meaning no missing data. If I see 8 non-null out of 10, that means 2 values are missing, which I must handle before analysis."

**DO (if time allows):**
```python
# Show data types separately
print("\nData types:")
print(employees_df.dtypes)
```

**SHOW:**
- Full info() output clearly visible
- Highlight non-null count column
- Point out data types (int64 vs object)
- Emphasize "this detects missing data"

---

### **Section 3: Using describe() for Statistics (1:15 - 1:45)** - 30 seconds

**SAY:**
> "Finally, describe() gives statistical summaries for numeric columns."

**DO:**
```python
print("Statistical summary:")
print(employees_df.describe())
```

**SAY:**
> "For Salary column: count shows 10 employees. Mean salary is about 80,800 dollars. The minimum is 62,000, maximum is 110,000. The 50th percentile—the median—is 75,000. This tells me salary range and distribution. If I see a max that's way higher than the 75th percentile, that could indicate an outlier."

**DO (optional):**
```python
# Show specific statistic
print(f"Average Salary: ${employees_df['Salary'].mean():,.2f}")
```

**SHOW:**
- Describe output with all statistics visible
- Highlight one column (e.g., Salary)
- Point out count, mean, min, max
- Mention quartiles (25%, 50%, 75%)

---

### **Section 4: Why This Matters (1:45 - 2:00)** - 15 seconds

**SAY:**
> "These three methods answer different questions: head() shows WHAT the data looks like, info() shows the STRUCTURE and detects missing values, and describe() shows DISTRIBUTIONS and ranges. Using all three takes 30 seconds but prevents hours of debugging. Always inspect before analyzing—it's a professional habit every Data Scientist follows."

**SHOW:**
- Quick recap visual (optional):
  - head() → Preview
  - info() → Structure
  - describe() → Statistics

---

## Success Criteria

Your video MUST demonstrate:

1. ✅ **Using `head()`** to preview first few rows
2. ✅ **Using `info()`** to show structure and detect missing data
3. ✅ **Using `describe()`** to show statistical summaries
4. ✅ **Explaining what each method reveals**
5. ✅ **Highlighting non-null counts** in info() output
6. ✅ **Interpreting at least one statistic** from describe() (e.g., mean, min, max)
7. ✅ **Emphasizing why inspection matters**

**Minimum requirement:** Show all 3 methods and explain what each one tells you.

---

## Three Complete Code Examples

### Example 1: Complete Inspection Workflow (Perfect for Video)

```python
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/employees.csv')

print("=" * 60)
print("COMPLETE INSPECTION WORKFLOW")
print("=" * 60)

# 1. Preview with head()
print("\n1. PREVIEW (head):")
print(df.head())

# 2. Structure with info()
print("\n2. STRUCTURE (info):")
df.info()

# 3. Statistics with describe()
print("\n3. STATISTICS (describe):")
print(df.describe())

print("\n" + "=" * 60)
print("✓ Inspection complete - ready to analyze!")
print("=" * 60)
```

**Expected Output:**
- First 5 rows displayed
- Info showing 10 rows, 6 columns, data types, no missing values
- Describe showing statistics for numeric columns (EmployeeID, Salary, YearsExperience)

---

### Example 2: Detecting Missing Data (Great for Advanced Demo)

```python
import pandas as pd

# Load sales data (has missing values)
sales_df = pd.read_csv('../data/raw/sales_data.csv')

print("Inspecting sales data:")
print("\n1. Preview:")
print(sales_df.head())

print("\n2. Structure check:")
sales_df.info()

print("\n3. Missing values explicit check:")
print(sales_df.isnull().sum())

print("\n⚠️ FINDING: CustomerCity has 2 missing values!")
print("   Action needed: Decide to drop or fill before analysis")
```

**Shows:** How info() reveals missing data (8 non-null instead of 10)

---

### Example 3: Focused Statistical Analysis

```python
import pandas as pd

df = pd.read_csv('../data/raw/employees.csv')

# Focus on Salary column
print("Salary Analysis:")
print(df['Salary'].describe())

print("\n📊 Key Insights:")
print(f"  Average: ${df['Salary'].mean():,.2f}")
print(f"  Median: ${df['Salary'].median():,.2f}")
print(f"  Range: ${df['Salary'].min():,.2f} to ${df['Salary'].max():,.2f}")
print(f"  Std Dev: ${df['Salary'].std():,.2f}")

print("\n✓ No extreme outliers detected")
```

**Shows:** Deep dive into one column's statistics

---

## Common Mistakes to Avoid

### ❌ DON'T:

1. **Only use head() and skip info()**
   - Problem: Miss hidden null values
   - Fix: Always use info() to check non-null counts

2. **Ignore data types in info()**
   - Problem: Numbers stored as 'object' break calculations
   - Fix: Always check dtypes, convert if needed

3. **Assume describe() shows all columns**
   - Problem: Only shows numeric columns by default
   - Fix: Use `describe(include='all')` for text columns too

4. **Skip inspection and jump to analysis**
   - Problem: Errors happen hours later, hard to debug
   - Fix: Make inspection mandatory first step

5. **Not check for missing values**
   - Problem: Operations fail or give wrong results with NaN
   - Fix: Check non-null count in info(), use `isnull().sum()`

### ✅ DO:

1. **Use all three methods every time**
   - head() for visual, info() for structure, describe() for stats

2. **Check non-null counts carefully**
   - If count < total rows, you have missing data

3. **Verify data types match expectations**
   - Numeric columns should be int64 or float64, not object

4. **Look for outliers in describe()**
   - Compare max to 75th percentile, min to 25th percentile

5. **Make inspection a habit**
   - Load → inspect → analyze (never skip inspect!)

---

## Timing Breakdown

| Section | Time | Content |
|---------|------|---------|
| **Intro** | 10s | What we're demonstrating |
| **head()** | 30s | Preview rows, show columns and values |
| **info()** | 35s | Structure, types, missing data |
| **describe()** | 30s | Statistics, ranges, distributions |
| **Why** | 15s | Importance of inspection |
| **Total** | **~2:00** | Complete demonstration |

---

## Troubleshooting

### Issue: Video is too long (>2:15)

**Solutions:**
- Focus on one dataset (employees only)
- Skip optional second examples
- Reduce explanation time on describe() to 25 seconds
- Cut intro to 8 seconds

### Issue: Output not visible on screen

**Solutions:**
- Zoom in your terminal/notebook
- Use smaller datasets (already provided)
- Show only first 3 rows with `head(3)`
- Focus video on terminal output area

### Issue: Not enough content for 2 minutes

**Solutions:**
- Add comparison: head(3) vs head(10)
- Show both employees and sales data
- Demonstrate tail() alongside head()
- Add explicit missing value check with `isnull().sum()`

### Issue: Explaining statistics is confusing

**Solutions:**
- Focus on 2-3 key stats: mean, min, max
- Use simple language: "average is...", "range is from...to..."
- Skip standard deviation if unclear
- Just mention quartiles without deep explanation

---

## Key Phrases to Use in Video

Essential vocabulary to demonstrate understanding:

1. **"head() shows the first few rows for a quick visual check"**
2. **"info() is the most important—it shows data types and detects missing values"**
3. **"The non-null count tells me if data is missing"**
4. **"describe() gives statistical summaries for numeric columns"**
5. **"Mean is the average, median is the middle value"**
6. **"Min and max show the range of values"**
7. **"Int64 means integers, object means text"**
8. **"Always check for null values before analysis"**
9. **"These three methods take 30 seconds but save hours"**
10. **"Inspection is mandatory after loading data"**

---

## After Recording: Checklist

Before submitting, verify your video includes:

- [ ] Clear screen capture showing all code and output
- [ ] Loading a DataFrame successfully
- [ ] Using `head()` and showing output
- [ ] Using `info()` and showing output
- [ ] Using `describe()` and showing output
- [ ] Explaining what head() reveals (preview, column names, sample values)
- [ ] Explaining what info() reveals (types, null counts, structure)
- [ ] Explaining what describe() reveals (statistics, ranges)
- [ ] Highlighting non-null count in info() output
- [ ] Interpreting at least one statistic (mean, min, or max)
- [ ] Mentioning why inspection prevents errors
- [ ] Speaking clearly and at moderate pace
- [ ] Duration between 1:45 and 2:15 (target: 2:00)
- [ ] All code executes without errors
- [ ] Output is readable on screen

---

## Quick Reference

### Three Essential Methods

| Method | Purpose | Key Output |
|--------|---------|------------|
| **`df.head()`** | Visual preview | First 5 rows (default) |
| **`df.info()`** | Structure check | Types, nulls, memory |
| **`df.describe()`** | Statistics | Mean, std, min, max, quartiles |

### What Each Method Tells You

| Method | Answers | Reveals |
|--------|---------|---------|
| **head()** | "What does my data look like?" | Sample values, column names |
| **info()** | "What is my data structure?" | Types, missing data, row count |
| **describe()** | "What are my distributions?" | Ranges, averages, spread |

### Common Statistics in describe()

| Statistic | Meaning | Use |
|-----------|---------|-----|
| **count** | Number of non-null values | Detect missing data |
| **mean** | Average value | Central tendency |
| **std** | Standard deviation | How spread out values are |
| **min** | Minimum value | Lower bound |
| **25%** | First quartile | 25% of data is below this |
| **50%** | Median (middle value) | Middle of distribution |
| **75%** | Third quartile | 75% of data is below this |
| **max** | Maximum value | Upper bound |

### Data Types Quick Reference

| dtype | Type | Example Values |
|-------|------|----------------|
| **int64** | Integers | 1, 100, 5000 |
| **float64** | Decimals | 3.14, 99.99 |
| **object** | Text/strings | "Alice", "Sales" |
| **bool** | True/False | True, False |
| **datetime64** | Dates | 2024-01-15 |

---

## Minimal Example (If Short on Time)

```python
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/employees.csv')

# Three essential methods
print("1. Preview:")
print(df.head())

print("\n2. Structure:")
df.info()

print("\n3. Statistics:")
print(df.describe())
```

**Narrate:**
- "Head shows first 5 rows"
- "Info shows 10 rows, 6 columns, no missing data"
- "Describe shows salary ranges from 62K to 110K"
- "These three methods are mandatory before analysis"

---

## Advanced Example (If Extra Time)

```python
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/employees.csv')

# Comprehensive inspection
print("=" * 50)
print("INSPECTION REPORT")
print("=" * 50)

print(f"\n📊 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"📋 Columns: {df.columns.tolist()}")

print("\n1️⃣ PREVIEW:")
print(df.head(3))

print("\n2️⃣ STRUCTURE:")
df.info()

print("\n3️⃣ STATISTICS:")
print(df.describe())

print("\n4️⃣ MISSING DATA:")
print(df.isnull().sum())

print("\n" + "=" * 50)
print("✅ Inspection complete - data is clean and ready!")
print("=" * 50)
```

---

## Final Reminders

1. **Practice once** before recording (run through code)
2. **Close unnecessary windows** for clean capture
3. **Zoom in** so output is clearly readable
4. **Speak confidently** - you know this material!
5. **Emphasize info()** - it's the most important method
6. **Show non-null counts** - detecting missing data is critical
7. **Time yourself** - aim for 1:50-2:10 range
8. **Test your video** - can you read all output when played back?

---

## Summary: What to Show

**Minimum Viable Demo (if time limited):**
1. Load DataFrame
2. Use head() - show output
3. Use info() - explain types and nulls
4. Use describe() - mention mean and range
5. Say why inspection matters

**Complete Demo (recommended):**
1. Load DataFrame
2. Use head() - point out columns, index, sample values
3. Use info() - highlight non-null counts, explain data types
4. Use describe() - interpret mean, min, max
5. Emphasize inspection prevents errors
6. Optional: show missing data example

**You're ready to record!** Focus on demonstrating that these three methods are mandatory for understanding data before analysis. Good luck! 🎥📊
