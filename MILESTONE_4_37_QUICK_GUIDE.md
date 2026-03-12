# Milestone 4.37: Computing Basic Summary Statistics for Individual Columns - 2-Minute Video Guide

**Total Time: 2 minutes (120 seconds)**

---

## SUCCESS CRITERIA

Your video must demonstrate **ALL 5 of these operations**:

1. [x] **Select One Numeric Column** from a DataFrame
2. [x] **Compute Basic Statistics** (`count`, `mean`, `median`, `min`, `max`)
3. [x] **Compute Spread Metrics** (`std`, `var`) and explain them simply
4. [x] **Compare With Another Numeric Column**
5. [x] **Interpret Results** (central tendency, spread, possible unusual values)

**Note:** If any of these 5 are missing, record again.

---

## VIDEO STRUCTURE & TIMING

### Introduction (0:00-0:10) - 10 seconds

**What to say:**
> "Hi, I am [Your Name]. This is Milestone 4.37 on computing summary statistics for individual columns in Pandas. I will show how to calculate and interpret basic statistics to understand data before deeper analysis."

**What to show:**
- Notebook title and milestone name
- Dataset loaded in notebook

---

### Section 1: Load Data and Identify Numeric Columns (0:10-0:30) - 20 seconds

**What to say:**
> "First, I load the sales dataset and check its numeric columns. Numeric columns are where summary statistics are most meaningful for central tendency and spread."

**What to show:**
```python
import pandas as pd

sales_df = pd.read_csv('../data/raw/sales_data.csv')
print(sales_df.head())
print("\nNumeric columns:", sales_df.select_dtypes(include='number').columns.tolist())
```

**Expected output (example):**
```
Numeric columns: ['OrderID', 'Quantity', 'Price']
```

**Key point:** "Identify numeric columns first, then analyze them one by one."

---

### Section 2: Compute Statistics for One Column (0:30-1:00) - 30 seconds

**What to say:**
> "Now I will focus on one numeric column, `Quantity`, and compute core summary statistics: count, mean, median, min, max, standard deviation, and variance."

**What to show:**
```python
qty_stats = sales_df['Quantity'].agg([
    'count', 'mean', 'median', 'min', 'max', 'std', 'var'
])
print(qty_stats)
```

**Expected output (values may vary):**
```
count     10.000000
mean       3.200000
median     2.500000
min        1.000000
max       10.000000
std        2.740641
var        7.511111
```

**Interpretation to say:**
- "Count tells me how many valid values were used."
- "Mean and median show center; if they differ, the data may be skewed."
- "Min and max show range boundaries."
- "Std and var show spread; larger values mean more variability."

---

### Section 3: Compare With Another Column (1:00-1:30) - 30 seconds

**What to say:**
> "Now I compare `Quantity` with `Price` to see how center and spread differ across columns. This helps identify which variable is more variable and where unusual values may exist."

**What to show:**
```python
comparison = sales_df[['Quantity', 'Price']].agg([
    'count', 'mean', 'median', 'min', 'max', 'std', 'var'
])
print(comparison)
```

**Interpretation to say:**
- "`Price` has much larger spread than `Quantity`, shown by higher std and variance."
- "A wider range often indicates more diverse values or potential outliers."

---

### Section 4: Interpret Mean vs Median and Outlier Sensitivity (1:30-1:50) - 20 seconds

**What to say:**
> "To build intuition, I add one extreme value to `Quantity` and compare mean and median again. Mean changes much more than median, so median is usually more robust with outliers."

**What to show:**
```python
qty_with_outlier = pd.concat([sales_df['Quantity'], pd.Series([50])], ignore_index=True)
print('Mean with outlier:', qty_with_outlier.mean())
print('Median with outlier:', qty_with_outlier.median())
```

**Key point:** "Do not interpret averages without checking spread and possible outliers."

---

### Wrap-Up (1:50-2:00) - 10 seconds

**What to say:**
> "Key takeaway: summary statistics are the first quantitative snapshot of a dataset. Always compute and interpret them before modeling so your analysis decisions are evidence-based."

**What to show:**
- Final summary cell
- Short recap of `Quantity` vs `Price` insights

---

## TROUBLESHOOTING GUIDE

### Problem 1: "Statistics look wrong"

**Cause:** Column is object/string, not numeric.

**Fix:**
```python
sales_df['Quantity'] = pd.to_numeric(sales_df['Quantity'], errors='coerce')
```

---

### Problem 2: "Mean and median are very different"

**Cause:** Possible skew or outliers.

**Fix:**
```python
print(sales_df['Quantity'].sort_values())
```

Then investigate extreme values before making conclusions.

---

### Problem 3: "Count is smaller than row count"

**Cause:** Missing values are present.

**Fix:**
```python
print(sales_df['Quantity'].isna().sum())
```

Always check missing values when interpreting statistics.

---

## FINAL CHECKLIST BEFORE SUBMITTING

- [ ] Loaded DataFrame successfully
- [ ] Selected at least one numeric column
- [ ] Computed basic summary statistics
- [ ] Explained each statistic in plain language
- [ ] Compared results with another numeric column
- [ ] Mentioned effect of outliers (mean vs median)
- [ ] Recorded a clear ~2-minute walkthrough video
- [ ] Included PR/video link as required

You are now ready to use summary statistics as a reliable first step in EDA.
