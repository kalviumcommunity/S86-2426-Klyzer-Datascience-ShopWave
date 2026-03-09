# Milestone 4.32: Selecting Rows and Columns Using Indexing and Slicing
## 2-Minute Video Demonstration Guide

---

## Video Requirements

**Duration:** ~2 minutes  
**Format:** Screen capture with visible code execution  
**Audience:** Data Science learners  
**Goal:** Demonstrate precise row and column selection using Pandas indexing and slicing

---

## 2-Minute Script with Timing

### Introduction (0:00 - 0:10) - 10 seconds

**SAY:**
> "Hi! Today I am demonstrating how to select rows and columns using indexing and slicing in Pandas. Selection is foundational because every cleaning and analysis step depends on selecting the right subset first."

**SHOW:**
- Notebook title visible
- Data loading cell visible

---

### Section 1: Select Columns by Name (0:10 - 0:40) - 30 seconds

**SAY:**
> "First, I select columns by name. A single column returns a Series, and multiple columns return a DataFrame."

**DO:**
```python
import pandas as pd

df = pd.read_csv('../data/raw/employees.csv')

name_series = df['Name']
selected_df = df[['Name', 'Department', 'Salary']]

print(type(name_series))
print(type(selected_df))
print(selected_df.head(3))
```

**SAY:**
> "This is the most common selection pattern and keeps code explicit and readable."

---

### Section 2: Select Rows by Position with iloc (0:40 - 1:10) - 30 seconds

**SAY:**
> "Next, I use iloc for position-based row selection. iloc uses zero-based positions and standard Python slicing behavior where the stop value is excluded."

**DO:**
```python
print(df.iloc[0])      # first row
print(df.iloc[2:6])    # rows at positions 2,3,4,5
print(df.iloc[[1, 4, 7]])
```

**SAY:**
> "I use iloc when I care about row position instead of row labels."

---

### Section 3: Select Rows by Label with loc (1:10 - 1:35) - 25 seconds

**SAY:**
> "Now I use loc for label-based selection. I will set EmployeeID as index so row labels are meaningful. loc label slicing is inclusive at both ends."

**DO:**
```python
df_label = df.set_index('EmployeeID')

print(df_label.loc[104])
print(df_label.loc[104:107])
```

**SAY:**
> "loc is explicit and ideal when your index labels carry business meaning."

---

### Section 4: Select Rows and Columns Together (1:35 - 1:50) - 15 seconds

**SAY:**
> "In real workflows, I usually select rows and columns together in one clear expression."

**DO:**
```python
print(df.iloc[1:5, [1, 2, 3]])
print(df_label.loc[103:106, ['Name', 'Department']])
```

---

### Section 5: Why This Matters (1:50 - 2:00) - 10 seconds

**SAY:**
> "Correct selection prevents silent mistakes. I always verify output shape and content after selection so downstream steps run on exactly the intended subset."

**SHOW:**
- Quick recap:
  - Column names -> explicit column selection
  - iloc -> position-based selection
  - loc -> label-based selection
  - combined selection -> practical workflow

---

## Success Criteria

Your video MUST demonstrate:

1. Selecting one column by name
2. Selecting multiple columns by name
3. Selecting rows by position with `iloc`
4. Selecting rows by label with `loc`
5. Selecting rows and columns together
6. Explaining when to use each approach

---

## Complete Code Example (Ready for Recording)

```python
import pandas as pd

# 1) Load data
df = pd.read_csv('../data/raw/employees.csv')
print('Loaded employees data')
print('Shape:', df.shape)

# 2) Column selection by name
print('\n' + '=' * 60)
print('COLUMN SELECTION')
print('=' * 60)
name_series = df['Name']
selected_df = df[['Name', 'Department', 'Salary']]
print('Single column type:', type(name_series))
print('Multiple columns type:', type(selected_df))
print(selected_df.head(3))

# 3) Row selection by position
print('\n' + '=' * 60)
print('ROW SELECTION BY POSITION (iloc)')
print('=' * 60)
print('First row:')
print(df.iloc[0])
print('\nRows 2 to 5 by position:')
print(df.iloc[2:6])
print('\nRows at positions 1, 4, 7:')
print(df.iloc[[1, 4, 7]])

# 4) Row selection by label
print('\n' + '=' * 60)
print('ROW SELECTION BY LABEL (loc)')
print('=' * 60)
df_label = df.set_index('EmployeeID')
print('Row with label 104:')
print(df_label.loc[104])
print('\nRows with labels 104 through 107 (inclusive):')
print(df_label.loc[104:107])

# 5) Combined row + column selection
print('\n' + '=' * 60)
print('COMBINED ROW + COLUMN SELECTION')
print('=' * 60)
print('Position-based subset: rows 1:5 and columns [Name, Department, Salary]')
print(df.iloc[1:5, [1, 2, 3]])
print('\nLabel-based subset: EmployeeID 103:106 and columns [Name, Department]')
print(df_label.loc[103:106, ['Name', 'Department']])

# 6) Basic verification after selection
subset = df_label.loc[103:106, ['Name', 'Department']]
print('\nVerification:')
print('Subset shape:', subset.shape)
print('Subset columns:', subset.columns.tolist())
```

---

## Common Mistakes to Avoid

- Mixing up `iloc` and `loc`
- Forgetting that `iloc` is zero-based and stop-exclusive
- Forgetting that `loc` label slicing is inclusive
- Using unclear chained selection expressions
- Not checking selection output after slicing

---

## Submission Checklist

- [ ] Notebook includes column selection by name
- [ ] Notebook includes row selection with `iloc`
- [ ] Notebook includes row selection with `loc`
- [ ] Notebook includes combined row-column selection
- [ ] Selection output is clearly explained
- [ ] ~2-minute walkthrough video recorded
- [ ] Video link ready for submission
- [ ] Pull Request created (if required)
