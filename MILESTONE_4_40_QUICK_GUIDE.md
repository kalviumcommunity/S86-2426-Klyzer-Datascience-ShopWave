# Milestone 4.40: Visualizing Data Distributions Using Boxplots - 2-Minute Video Guide

**Total Time: 2 minutes (120 seconds)**

---

## SUCCESS CRITERIA

Your video must demonstrate **ALL 5 of these operations**:

1. [x] **Load a DataFrame** and select numeric column(s)
2. [x] **Create a Boxplot** for a single numeric column
3. [x] **Explain Median and Quartiles** (Q1, median, Q3, IQR)
4. [x] **Identify Potential Outliers** using points beyond whiskers
5. [x] **Compare Boxplots Across Columns** and interpret spread differences

**Note:** If any of these 5 are missing, record again.

---

## VIDEO STRUCTURE & TIMING

### Introduction (0:00-0:10) - 10 seconds

**What to say:**
> "Hi, I am [Your Name]. This is Milestone 4.40 on visualizing data distributions using boxplots. I will show how boxplots summarize spread, central tendency, and outliers across numeric columns."

**What to show:**
- Notebook title
- Dataset loaded in notebook

---

### Section 1: Load Data and Numeric Columns (0:10-0:30) - 20 seconds

**What to say:**
> "First, I load the sales dataset and identify numeric columns. Boxplots work on numeric data and provide a compact distribution summary."

**What to show:**
```python
import pandas as pd
import matplotlib.pyplot as plt

sales_df = pd.read_csv('../data/raw/sales_data.csv')
numeric_cols = sales_df.select_dtypes(include='number').columns.tolist()

print('Numeric columns:', numeric_cols)
print(sales_df[numeric_cols].head())
```

**Key point:** "Boxplots are for numeric distributions, not category counts."

---

### Section 2: Single-Column Boxplot (0:30-1:00) - 30 seconds

**What to say:**
> "Now I create a boxplot for `Quantity`. The line inside the box is the median. The box spans Q1 to Q3, and the whiskers show the non-outlier range."

**What to show:**
```python
plt.figure(figsize=(6, 4))
plt.boxplot(sales_df['Quantity'], vert=True, patch_artist=True)
plt.title('Boxplot of Quantity')
plt.ylabel('Quantity')
plt.tight_layout()
plt.show()
```

**Interpretation to say:**
- "Median is the center line in the box."
- "Box height represents IQR, which is Q3 minus Q1."
- "Points outside whiskers are potential outliers."

---

### Section 3: Explain Quartiles and IQR (1:00-1:25) - 25 seconds

**What to say:**
> "I now compute Q1, median, Q3, and IQR numerically to support what the boxplot shows visually."

**What to show:**
```python
q1 = sales_df['Quantity'].quantile(0.25)
median = sales_df['Quantity'].quantile(0.50)
q3 = sales_df['Quantity'].quantile(0.75)
iqr = q3 - q1

print('Q1:', q1)
print('Median:', median)
print('Q3:', q3)
print('IQR:', iqr)
```

**Interpretation tip:**
- Smaller IQR means tighter middle spread
- Larger IQR means more variability in middle 50%

---

### Section 4: Compare Boxplots Across Columns (1:25-1:50) - 25 seconds

**What to say:**
> "Now I compare boxplots for `Quantity` and `Price`. This side-by-side view makes differences in spread and outlier behavior easy to spot."

**What to show:**
```python
plt.figure(figsize=(8, 4))
plt.boxplot(
    [sales_df['Quantity'], sales_df['Price']],
    labels=['Quantity', 'Price'],
    patch_artist=True
)
plt.title('Boxplot Comparison: Quantity vs Price')
plt.ylabel('Value')
plt.tight_layout()
plt.show()
```

**Interpretation to say:**
- "Wider box and longer whiskers indicate greater spread."
- "Outlier points help flag unusual observations for investigation."

---

### Wrap-Up (1:50-2:00) - 10 seconds

**What to say:**
> "Key takeaway: boxplots provide a compact and powerful way to compare distributions, center, spread, and potential outliers before deeper analysis."

**What to show:**
- Final takeaway cell
- One short insight comparing `Quantity` and `Price`

---

## TROUBLESHOOTING GUIDE

### Problem 1: "Outliers are not visible"

**Cause:** There may be no points beyond whiskers, or scale may hide them.

**Fix:**
```python
plt.boxplot(sales_df['Quantity'], showfliers=True)
plt.show()
```

---

### Problem 2: "Hard to compare columns"

**Cause:** Columns may be on very different scales.

**Fix:**
- Compare one pair at a time
- Support visual comparison with quartile/IQR statistics

---

### Problem 3: "Assuming outliers are data errors"

**Clarification:**
- Outliers are unusual values, not automatically mistakes
- Investigate context before removing anything

Use boxplots to ask questions, not to make automatic deletions.

---

## FINAL CHECKLIST BEFORE SUBMITTING

- [ ] Loaded DataFrame successfully
- [ ] Selected numeric column(s)
- [ ] Created a single-column boxplot
- [ ] Explained median, quartiles, and IQR
- [ ] Identified potential outliers visually
- [ ] Compared boxplots across columns
- [ ] Recorded a clear ~2-minute walkthrough video
- [ ] Included PR/video link as required

You are now ready to use boxplots as a core distribution-comparison tool in EDA.
