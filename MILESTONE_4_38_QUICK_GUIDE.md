# Milestone 4.38: Comparing Distributions Across Multiple Columns - 2-Minute Video Guide

**Total Time: 2 minutes (120 seconds)**

---

## SUCCESS CRITERIA

Your video must demonstrate **ALL 5 of these operations**:

1. [x] **Load a DataFrame** with multiple numeric columns
2. [x] **Compute Summary Statistics** for multiple columns together
3. [x] **Compare Central Tendency** (mean and median)
4. [x] **Compare Spread** (range, standard deviation, variance)
5. [x] **Interpret Differences** and identify possible anomalies conceptually

**Note:** If any of these 5 are missing, record again.

---

## VIDEO STRUCTURE & TIMING

### Introduction (0:00-0:10) - 10 seconds

**What to say:**
> "Hi, I am [Your Name]. This is Milestone 4.38 on comparing distributions across multiple columns in Pandas. I will compare central tendency and spread to understand how variables behave relative to each other."

**What to show:**
- Notebook title
- Dataset and objective briefly

---

### Section 1: Load Data and Select Numeric Columns (0:10-0:30) - 20 seconds

**What to say:**
> "First, I load the dataset and identify numeric columns. Distribution comparison only makes sense when we compare variables using consistent statistical summaries."

**What to show:**
```python
import pandas as pd

sales_df = pd.read_csv('../data/raw/sales_data.csv')
numeric_cols = ['OrderID', 'Quantity', 'Price']

print(sales_df.head())
print('\nNumeric columns used:', numeric_cols)
```

**Key point:** "We compare distributions, not raw rows in isolation."

---

### Section 2: Compare Central Tendency (0:30-1:00) - 30 seconds

**What to say:**
> "Now I compare means and medians across columns. Mean gives the average, and median gives the middle value. If mean and median are far apart, that may indicate skew or unusual values."

**What to show:**
```python
central = sales_df[numeric_cols].agg(['mean', 'median']).T
print('Central tendency comparison:')
print(central)
```

**Interpretation to say:**
- "Columns with close mean and median are often more balanced."
- "Larger gaps between mean and median can signal skew."

---

### Section 3: Compare Spread and Variability (1:00-1:30) - 30 seconds

**What to say:**
> "Next I compare spread using min, max, range, standard deviation, and variance. This shows which columns are stable and which are more volatile."

**What to show:**
```python
spread = sales_df[numeric_cols].agg(['min', 'max', 'std', 'var']).T
spread['range'] = spread['max'] - spread['min']
print('Spread and variability comparison:')
print(spread[['min', 'max', 'range', 'std', 'var']])
```

**Interpretation to say:**
- "Higher range/std/var means greater variability."
- "Lower spread often means more consistency."

---

### Section 4: Detect Patterns and Anomalies Conceptually (1:30-1:50) - 20 seconds

**What to say:**
> "Now I flag columns where mean and median differ noticeably and where spread is unusually high. This helps raise questions for deeper EDA without jumping to conclusions."

**What to show:**
```python
summary = sales_df[numeric_cols].describe().T
summary['range'] = summary['max'] - summary['min']
summary['mean_minus_median'] = summary['mean'] - summary['50%']

print(summary[['count', 'mean', '50%', 'mean_minus_median', 'range', 'std']])
```

**Key point:** "EDA is about asking better questions, not making final claims too early."

---

### Wrap-Up (1:50-2:00) - 10 seconds

**What to say:**
> "Key takeaway: comparing distributions across columns reveals patterns you cannot see from single-column analysis. This comparison step is essential before deeper analysis or modeling."

**What to show:**
- Final comparison table
- 1 to 2 verbal insights from results

---

## TROUBLESHOOTING GUIDE

### Problem 1: "Some columns are missing from results"

**Cause:** Non-numeric columns are excluded from numeric aggregation.

**Fix:**
```python
print(sales_df.select_dtypes(include='number').columns.tolist())
```

---

### Problem 2: "Statistics seem too large to compare directly"

**Cause:** Columns are on different scales (for example `OrderID` vs `Quantity`).

**Fix:**
- Compare patterns within each column (mean vs median, range, std)
- Avoid saying one column is "better" just because numbers are larger

---

### Problem 3: "Mean and median do not match"

**Cause:** Likely skew or outliers.

**Fix:**
```python
for col in numeric_cols:
    print(col, 'mean=', sales_df[col].mean(), 'median=', sales_df[col].median())
```

Use this as a signal for deeper investigation.

---

## FINAL CHECKLIST BEFORE SUBMITTING

- [ ] Loaded a DataFrame with multiple numeric columns
- [ ] Computed summary statistics for multiple columns
- [ ] Compared means and medians across columns
- [ ] Compared range/std/variance across columns
- [ ] Interpreted differences without overclaiming
- [ ] Mentioned possible anomalies conceptually
- [ ] Recorded a clear ~2-minute walkthrough video
- [ ] Included PR/video link as required

You are now ready to compare distributions and build stronger EDA intuition.
