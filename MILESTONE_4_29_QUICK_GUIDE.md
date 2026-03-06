# Milestone 4.29: Loading CSV Data into Pandas DataFrames
## 2-Minute Video Demonstration Guide

---

## Video Requirements

**Duration:** ~2 minutes  
**Format:** Screen capture with visible code execution  
**Audience:** Data Science learners  
**Goal:** Demonstrate CSV loading, inspection, and issue recognition

---

## 2-Minute Script with Timing

### **Introduction (0:00 - 0:10)** - 10 seconds

**SAY:**
> "Hi! Today I'm demonstrating CSV loading in Pandas—the most common way to start data analysis. Loading data correctly is critical because downstream errors often begin here. Let's load a CSV file and inspect it properly."

**SHOW:**
- Your notebook open with title visible
- Import statements ready

---

### **Section 1: Loading a CSV File (0:10 - 0:40)** - 30 seconds

**SAY:**
> "First, I'll load a standard CSV file using pd.read_csv(). This is the products CSV with comma-separated values and a header row."

**DO:**
```python
import pandas as pd

# Load CSV file
products_df = pd.read_csv('../data/raw/products.csv')
print("✓ CSV loaded successfully!")
print(products_df)
```

**SAY:**
> "Notice how the first row became column names—Product, Price, Stock, Category—and the remaining rows became data with automatic index zero, one, two, and so on."

**SHOW:**
- Clear output of the DataFrame
- Point out column names at the top
- Point out index on the left (0, 1, 2...)
- Highlight how CSV rows → DataFrame rows

---

### **Section 2: Inspecting the Loaded Data (0:40 - 1:10)** - 30 seconds

**SAY:**
> "Here's the most important part: ALWAYS inspect data after loading. I'll use four key methods."

**DO:**
```python
# 1. Check shape
print(f"Shape: {products_df.shape}")

# 2. Check columns
print(f"Columns: {products_df.columns.tolist()}")

# 3. Use info() - most important!
products_df.info()

# 4. Check for missing values
print(products_df.isnull().sum())
```

**SAY:**
> "Shape shows five rows and four columns. Info tells me the column names, data types—Price and Stock are numeric, Product and Category are text objects—and there are no missing values. This inspection step catches issues early."

**SHOW:**
- Each method's output clearly
- Emphasize `.info()` as comprehensive check
- Highlight "5 non-null" confirming no missing data

---

### **Section 3: Recognizing a Common Issue (1:10 - 1:45)** - 35 seconds

**SAY:**
> "Now let me show a common loading issue: wrong delimiter. This CSV uses semicolons instead of commas."

**DO:**
```python
# WRONG: Default comma delimiter
wrong_df = pd.read_csv('../data/raw/sales_semicolon.csv')
print("Loaded with wrong delimiter:")
print(wrong_df.head())
print(f"Columns: {wrong_df.columns.tolist()}")
```

**SAY:**
> "See the problem? Everything loaded into one column because Pandas used comma as delimiter, but the file uses semicolons. This is why inspection is critical."

**DO:**
```python
# CORRECT: Specify semicolon
correct_df = pd.read_csv('../data/raw/sales_semicolon.csv', sep=';')
print("\nLoaded with correct delimiter:")
print(correct_df.head())
print(f"Columns: {correct_df.columns.tolist()}")
```

**SAY:**
> "By specifying sep equals semicolon, now the data loads correctly into separate columns."

**SHOW:**
- Side-by-side comparison of wrong vs correct loading
- Highlight how first attempt has 1 column
- Highlight how second attempt has 4 columns

---

### **Section 4: Why This Matters (1:45 - 2:00)** - 15 seconds

**SAY:**
> "CSV loading is the foundation of data analysis. Always inspect with info, head, and shape immediately after loading. Catching errors here prevents hours of debugging later. Most data problems start at loading—master this skill, and your analysis will be reliable from the start."

**SHOW:**
- Final successful DataFrame
- Checklist overlay (optional):
  - ✓ Load CSV
  - ✓ Check shape
  - ✓ Check columns
  - ✓ Use .info()
  - ✓ Check for nulls

---

## Success Criteria

Your video MUST demonstrate:

1. ✅ **Loading a CSV file** with `pd.read_csv()`
2. ✅ **Displaying the loaded DataFrame** (showing rows and columns)
3. ✅ **Checking shape** with `.shape`
4. ✅ **Checking column names** with `.columns`
5. ✅ **Using `.info()`** to get comprehensive overview
6. ✅ **Showing a loading issue** (e.g., wrong delimiter, no header)
7. ✅ **Fixing the issue** with appropriate parameter

**Minimum requirement:** Show at least 5 of the 7 points above.

---

## Three Complete Code Examples

### Example 1: Standard CSV Loading (Perfect for Video)

```python
import pandas as pd

# Load CSV
df = pd.read_csv('../data/raw/products.csv')

# Immediate inspection
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nFirst 3 rows:")
print(df.head(3))

print("\nComprehensive info:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())
```

**Expected Output:**
```
Shape: (5, 4)
Columns: ['Product', 'Price', 'Stock', 'Category']

First 3 rows:
    Product   Price  Stock     Category
0    Laptop  999.99     15  Electronics
1     Mouse   29.99    150  Electronics
2  Keyboard   79.99     80  Electronics

Comprehensive info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Product   5 non-null      object 
 1   Price     5 non-null      float64
 2   Stock     5 non-null      int64  
 3   Category  5 non-null      object 
dtypes: float64(1), int64(1), object(2)

Missing values:
Product     0
Price       0
Stock       0
Category    0
dtype: int64
```

---

### Example 2: Wrong Delimiter Issue (Great for Problem Demonstration)

```python
import pandas as pd

# WRONG: Using default comma
print("Loading with WRONG delimiter:")
wrong_df = pd.read_csv('../data/raw/sales_semicolon.csv')
print(wrong_df.head())
print(f"Columns: {wrong_df.columns.tolist()}")
print("⚠️ Problem: Only 1 column!")

# CORRECT: Specify semicolon
print("\nLoading with CORRECT delimiter:")
right_df = pd.read_csv('../data/raw/sales_semicolon.csv', sep=';')
print(right_df.head())
print(f"Columns: {right_df.columns.tolist()}")
print("✓ Fixed: Now 4 columns!")
```

**Shows:** How to recognize and fix delimiter issues

---

### Example 3: CSV Without Header (Advanced Issue)

```python
import pandas as pd

# WRONG: Pandas assumes first row is header
print("Without specifying no header:")
wrong_df = pd.read_csv('../data/raw/data_no_header.csv')
print(wrong_df)
print("⚠️ Problem: First data row became column names!")

# CORRECT: Specify no header + custom names
print("\nWith header=None and custom names:")
right_df = pd.read_csv(
    '../data/raw/data_no_header.csv',
    header=None,
    names=['Name', 'Department', 'Salary']
)
print(right_df)
print("✓ Fixed: All rows are data, custom columns applied!")
```

**Shows:** How to handle CSVs without header rows

---

## Common Mistakes to Avoid

### ❌ DON'T:

1. **Skip inspection after loading**
   - Problem: Silent errors go unnoticed
   - Fix: Always use `.info()` and `.head()`

2. **Assume file loaded correctly**
   - Problem: Wrong delimiter, missing header
   - Fix: Check column count and names

3. **Guess at file structure**
   - Problem: Wrong parameters used
   - Fix: Open CSV in text editor first to see structure

4. **Use absolute paths**
   - Problem: Code breaks on other machines
   - Fix: Use relative paths: `'../data/raw/file.csv'`

5. **Forget to check for missing data**
   - Problem: NaN values cause errors later
   - Fix: `df.isnull().sum()` immediately

### ✅ DO:

1. **Inspect immediately after loading**
   - Use: `.shape`, `.columns`, `.info()`, `.head()`

2. **Check for expected structure**
   - Verify: Row count, column count, column names

3. **Look at the raw CSV first**
   - Open in text editor to see delimiter, header

4. **Use relative paths**
   - Best practice: `'../data/raw/file.csv'`

5. **Check data types**
   - Use: `.dtypes` or `.info()`

---

## Timing Breakdown

| Section | Time | Content |
|---------|------|---------|
| **Intro** | 10s | What we're demonstrating |
| **Loading** | 30s | Load CSV, show DataFrame |
| **Inspection** | 30s | Shape, columns, info, nulls |
| **Issue** | 35s | Show problem + fix |
| **Why** | 15s | Importance of correct loading |
| **Total** | **~2:00** | Complete demonstration |

---

## Troubleshooting

### Issue: Video is too long (>2:15)

**Solutions:**
- Skip advanced examples (focus on one issue)
- Reduce explanation time
- Pre-run cells to avoid waiting for output
- Cut the "why this matters" section to 10 seconds

### Issue: Can't find CSV files

**Solutions:**
- Run from `notebooks/` directory
- Use path: `'../data/raw/file.csv'`
- Check files exist with `ls ../data/raw/`

### Issue: Output too long for video

**Solutions:**
- Use `.head(3)` instead of `.head()`
- Show only key parts of `.info()` output
- Zoom in so text is readable

### Issue: Not enough content for 2 minutes

**Solutions:**
- Add second CSV loading example
- Show both correct and incorrect loading
- Demonstrate 2-3 inspection methods
- Include missing data check

---

## Key Phrases to Use in Video

Essential vocabulary to demonstrate understanding:

1. **"CSV stands for Comma-Separated Values"**
2. **"The first row is the header with column names"**
3. **"I'll use pd.read_csv() to load the file"**
4. **"Always inspect data immediately after loading"**
5. **"The shape shows rows and columns"**
6. **"Info gives a comprehensive overview"**
7. **"This shows there are no missing values"**
8. **"Wrong delimiter is a common loading issue"**
9. **"Inspection catches errors early"**
10. **"CSV loading is the foundation of data analysis"**

---

## After Recording: Checklist

Before submitting, verify your video includes:

- [ ] Clear screen capture showing all code and output
- [ ] Loading at least one CSV file successfully
- [ ] Displaying the loaded DataFrame
- [ ] Using `.shape` to show dimensions
- [ ] Using `.columns` to show column names  
- [ ] Using `.info()` for comprehensive check
- [ ] Checking for missing values with `.isnull().sum()`
- [ ] Demonstrating at least one loading issue (delimiter, header, path)
- [ ] Showing how to fix the issue with parameters
- [ ] Explaining why inspection matters
- [ ] Speaking clearly and at moderate pace
- [ ] Duration between 1:45 and 2:15 (target: 2:00)
- [ ] All code executes without errors
- [ ] Output is readable on screen
- [ ] Face visible (if screen-facing requirement met)

---

## Quick Reference

### Essential Inspection Methods

| Method | Purpose | Usage |
|--------|---------|-------|
| `.head()` | Preview first 5 rows | `df.head()` |
| `.tail()` | Preview last 5 rows | `df.tail()` |
| `.shape` | Get dimensions | `df.shape` |
| `.columns` | Get column names | `df.columns.tolist()` |
| `.info()` | Comprehensive overview | `df.info()` |
| `.describe()` | Statistical summary | `df.describe()` |
| `.dtypes` | Column data types | `df.dtypes` |
| `.isnull().sum()` | Count missing values | `df.isnull().sum()` |

### Common `read_csv()` Parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `sep` | Specify delimiter | `sep=';'` |
| `header` | Header row index | `header=None` |
| `names` | Custom column names | `names=['A', 'B']` |
| `skiprows` | Skip N rows | `skiprows=2` |
| `usecols` | Load specific columns | `usecols=['Name', 'Age']` |
| `index_col` | Use column as index | `index_col='ID'` |
| `dtype` | Specify data types | `dtype={'Age': int}` |

### Loading Issues Quick Reference

| Symptom | Issue | Fix |
|---------|-------|-----|
| Only 1 column | Wrong delimiter | `sep=';'` or `sep='\t'` |
| First row missing | No header specified | `header=None, names=[...]` |
| FileNotFoundError | Wrong path | Check path, use relative |
| Column access fails | Extra spaces | `df.columns.str.strip()` |
| Numbers as 'object' | Mixed data types | Check with `.dtypes` |

---

## Final Reminders

1. **Practice your demo** before recording (run through once)
2. **Close unnecessary windows** for clean screen capture
3. **Zoom in** so code and output are clearly visible
4. **Speak clearly** and at moderate pace
5. **Show enthusiasm** - CSV loading is foundational!
6. **Time yourself** - aim for 1:50-2:10 range
7. **Test your video** - can you read all text when played back?

---

## Summary: What to Show

**Minimum Viable Demo (if time limited):**
1. Load one CSV file
2. Show the DataFrame
3. Use `.shape` and `.info()`
4. Explain why inspection matters

**Complete Demo (recommended):**
1. Load CSV successfully
2. Show shape, columns, head, info
3. Check for missing values
4. Demonstrate one loading issue (delimiter or header)
5. Fix the issue with correct parameter
6. Explain importance of correct loading

**You're ready to record!** Focus on demonstrating that you understand CSV loading is critical and that inspection prevents errors. Good luck! 🎥📊
