# Milestone 4.31: Understanding Data Shapes and Column Data Types
## 2-Minute Video Demonstration Guide

---

## Video Requirements

**Duration:** ~2 minutes  
**Format:** Screen capture with visible code execution  
**Audience:** Data Science learners  
**Goal:** Demonstrate confident DataFrame structure inspection before cleaning or analysis

---

## 2-Minute Script with Timing

### Introduction (0:00 - 0:10) - 10 seconds

**SAY:**
> "Hi! Today I am demonstrating how to inspect DataFrame shape and column data types in Pandas. This is the first structural check I do after loading data because it prevents downstream errors."

**SHOW:**
- Notebook title visible
- Data import cell visible

---

### Section 1: Check DataFrame Shape (0:10 - 0:45) - 35 seconds

**SAY:**
> "First, I check shape. Shape returns a tuple in the format: rows, columns. Rows are observations or records, and columns are attributes or features."

**DO:**
```python
import pandas as pd

sales_df = pd.read_csv('../data/raw/sales_data.csv')

print('Shape:', sales_df.shape)
rows, cols = sales_df.shape
print('Rows:', rows)
print('Columns:', cols)
```

**SAY:**
> "This dataset has 10 rows and 6 columns. That means 10 order records and 6 attributes per record."

**SHOW:**
- Shape output clearly visible
- Explicit rows and columns printout

---

### Section 2: Inspect Column Data Types (0:45 - 1:20) - 35 seconds

**SAY:**
> "Next, I inspect data types using dtypes. Types control which operations are valid. Numeric columns support math operations, while object columns usually store text or mixed values."

**DO:**
```python
print('\nColumn data types:')
print(sales_df.dtypes)

print('\nType counts:')
print(sales_df.dtypes.value_counts())
```

**SAY:**
> "I can see integer, float, and object columns. This helps me know what can be aggregated, grouped, or converted later if needed."

**SHOW:**
- dtypes output
- Count of each dtype

---

### Section 3: Detect Type-Related Issues Early (1:20 - 1:45) - 25 seconds

**SAY:**
> "Now I look for warning signs: numeric-looking columns stored as object, missing values, or mixed values that can break analysis."

**DO:**
```python
print('\nMissing values per column:')
print(sales_df.isna().sum())

text_like_cols = sales_df.select_dtypes(include=['object', 'string', 'str']).columns.tolist()
print('\nText-like columns:', text_like_cols)
```

**SAY:**
> "If a text-like column should be numeric, that is a red flag. Missing values can also affect behavior, so I note those before any processing."

**SHOW:**
- Missing value counts
- Object columns list

---

### Section 4: Why This Matters (1:45 - 2:00) - 15 seconds

**SAY:**
> "Shape and data types are the blueprint of a dataset. If I skip this check, I can make wrong assumptions and produce incorrect analysis. By checking structure first, I make reliable decisions in later steps."

**SHOW:**
- Final recap:
  - Shape -> dataset size
  - Rows vs columns -> structure
  - dtypes -> valid operations
  - early issue detection -> fewer bugs

---

## Success Criteria

Your video MUST demonstrate:

1. `DataFrame.shape` inspection
2. Correct interpretation of rows and columns
3. `DataFrame.dtypes` inspection
4. High-level understanding of common data types
5. Detection mindset for suspicious or unexpected types
6. Explanation of why shape and types matter before processing

---

## Complete Code Example (Ready for Recording)

```python
import pandas as pd

# 1. Load data
sales_df = pd.read_csv('../data/raw/sales_data.csv')

# 2. Shape and structure
print('=' * 60)
print('SHAPE INSPECTION')
print('=' * 60)
print('Shape:', sales_df.shape)
rows, cols = sales_df.shape
print('Rows:', rows)
print('Columns:', cols)

# 3. Data types
print('\n' + '=' * 60)
print('DTYPE INSPECTION')
print('=' * 60)
print(sales_df.dtypes)
print('\nType counts:')
print(sales_df.dtypes.value_counts())

# 4. Early warning checks
print('\n' + '=' * 60)
print('EARLY ISSUE DETECTION')
print('=' * 60)
print('Missing values per column:')
print(sales_df.isna().sum())

text_like_cols = sales_df.select_dtypes(include=['object', 'string', 'str']).columns.tolist()
print('\nText-like columns:', text_like_cols)

print('\nInterpretation:')
print('- Shape tells us dataset size: rows = records, columns = attributes')
print('- dtypes tell us what operations are valid for each column')
print('- Missing values and text-like columns should be reviewed before processing')
```

---

## Common Mistakes to Avoid

- Assuming shape without checking `.shape`
- Confusing rows and columns in the shape tuple
- Assuming numeric-looking values are numeric dtype
- Ignoring text-like columns that should be numbers
- Starting analysis before checking missing values and dtypes

---

## Submission Checklist

- [ ] Notebook demonstrates shape inspection
- [ ] Notebook demonstrates dtype inspection
- [ ] Explanation of rows vs columns included
- [ ] Type-related issue awareness explained
- [ ] ~2-minute walkthrough video recorded
- [ ] Video link ready for submission
- [ ] Pull Request created (if required)
