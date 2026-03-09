# Milestone 4.33: Detecting Missing Values in DataFrames
## 2-Minute Video Demonstration Guide

## Goal
Demonstrate how to detect and summarize missing values in a Pandas DataFrame before any cleaning or imputation.

## What To Show
1. Load a DataFrame.
2. Detect missing values with `isna()` / `isnull()`.
3. Count missing values per column.
4. Inspect rows that contain missing entries.
5. Explain why early detection matters.

## 2-Minute Script
### 0:00-0:15 Intro
"In this demo, I am checking missing values in a DataFrame. Missing-value detection is a data health check that should happen before analysis or cleaning."

### 0:15-0:40 Load Data
- Load `sales_data.csv`.
- Show shape and first rows.

### 0:40-1:10 Detect Missing Values
- Show `df.isna()` (or top rows of it).
- Explain that `True` means the value is missing.

### 1:10-1:35 Count Missing Values
- Use `df.isna().sum()` for counts.
- Optional: show missing percentage.
- Point out which columns have missing data.

### 1:35-1:55 Inspect Affected Rows
- Filter rows where any value is missing using `df[df.isna().any(axis=1)]`.
- Briefly interpret what is missing and where.

### 1:55-2:00 Close
"Detection comes first. Once we know where data is incomplete, we can choose a proper cleaning strategy intentionally."

## Complete Demo Code
```python
import pandas as pd

# 1) Load

df = pd.read_csv('../data/raw/sales_data.csv')
print('Shape:', df.shape)
print(df.head())

# 2) Detect

missing_mask = df.isna()
print('\nMissing-value mask (first 5 rows):')
print(missing_mask.head())

# 3) Summarize

missing_count = df.isna().sum()
missing_percent = (missing_count / len(df) * 100).round(2)

summary = pd.DataFrame({
    'missing_count': missing_count,
    'missing_percent': missing_percent
})

print('\nMissing-value summary by column:')
print(summary)

# 4) Row-level inspection

rows_with_missing = df[df.isna().any(axis=1)]
print('\nRows containing at least one missing value:')
print(rows_with_missing)
print('Count of rows with missing values:', len(rows_with_missing))
```

## Common Mistakes To Avoid
- Assuming CSV files are complete without checking.
- Ignoring nulls while computing stats.
- Treating empty strings and missing values as always identical.
- Starting cleaning before understanding missingness severity.

## Submission Checklist
- [ ] DataFrame loaded
- [ ] Missing values detected with Pandas methods
- [ ] Missing counts per column shown
- [ ] Rows with missing entries inspected
- [ ] Why detection matters explained
- [ ] ~2-minute video recorded
- [ ] Video link submitted