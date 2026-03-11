# Milestone 4.34: Handling Missing Values - 2-Minute Video Guide

**Total Time: 2 minutes (120 seconds)**

---

## SUCCESS CRITERIA

Your video must demonstrate **ALL 5 of these operations**:

1. ✅ **Detect Missing Values** using `isnull().sum()`
2. ✅ **Drop Rows** with missing data using `dropna()`
3. ✅ **Fill Numeric Values** using `fillna()` with median
4. ✅ **Fill Categorical Values** using `fillna()` with constant or mode
5. ✅ **Compare Results** (show shape before/after and justify strategy)

**Note:** If any of these 5 are missing, record again.

---

## VIDEO STRUCTURE & TIMING

### Introduction (0:00-0:10) • 10 seconds

**What to say:**
> "Hi, I'm [Your Name]. This is Milestone 4.34—Handling Missing Values Using Drop and Fill Strategies. I'll show you how to detect missing data, when to drop it, when to fill it, and how to choose the right strategy."

**What to show:**
- Milestone title slide or notebook open
- Confident, clear voice

---

### Section 1: Detecting Missing Values (0:10-0:30) • 20 seconds

**What to say:**
> "First, I'll load a dataset with missing values and inspect what's missing. Using `isnull().sum()`, I can see which columns have missing data and how many values are missing in each column."

**What to show:**
```python
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/survey_data.csv')

# Inspect missing values
print("Missing values per column:")
print(df.isnull().sum())

# Show percentage missing
missing_pct = (df.isnull().sum() / len(df)) * 100
print("\nMissing percentage:")
print(missing_pct)
```

**Expected output:**
```
Missing values per column:
RespondentID    0
Age             2
Income          3
Education       1
Satisfaction    1
City            2
dtype: int64

Missing percentage:
RespondentID     0.0
Age             20.0
Income          30.0
Education       10.0
Satisfaction    10.0
City            20.0
dtype: float64
```

**Key point:** "Income has 30% missing—much more than other columns."

---

### Section 2: Strategy 1 - Dropping Rows (0:30-0:55) • 25 seconds

**What to say:**
> "Now I'll demonstrate the drop strategy. First, dropping ALL rows with ANY missing value loses 70% of data—too aggressive! Instead, I'll use a targeted approach: drop only rows where critical columns like Age or Income are missing. This preserves more data."

**What to show:**
```python
# AVOID: Dropping all rows with ANY missing
df_drop_all = df.dropna()
print(f"After dropna(): {df_drop_all.shape}")
print(f"Data lost: {len(df) - len(df_drop_all)} rows ({((len(df) - len(df_drop_all)) / len(df) * 100):.1f}%)")

print("\n---Better Approach---")

# BETTER: Drop only if critical columns are missing
df_drop_critical = df.dropna(subset=['Age', 'Income'])
print(f"After dropping rows with missing Age or Income: {df_drop_critical.shape}")
print(f"Data lost: {len(df) - len(df_drop_critical)} rows ({((len(df) - len(df_drop_critical)) / len(df) * 100):.1f}%)")
```

**Expected output:**
```
After dropna(): (3, 6)
Data lost: 7 rows (70.0%)

---Better Approach---
After dropping rows with missing Age or Income: (5, 6)
Data lost: 5 rows (50.0%)
```

**Key point:** "Targeted dropping balances data quality and data quantity."

---

### Section 3: Strategy 2 - Filling Values (0:55-1:35) • 40 seconds

**What to say:**
> "For the fill strategy, I use different approaches based on data type. For numeric columns like Age and Income, I fill with the median—it's robust to outliers. For categorical columns like City and Education, I fill with the mode or a constant like 'Unknown'."

**What to show:**
```python
# Create a copy for filling
df_fill = df.copy()

# Fill numeric columns with median
median_age = df_fill['Age'].median()
median_income = df_fill['Income'].median()

df_fill['Age'] = df_fill['Age'].fillna(median_age)
df_fill['Income'] = df_fill['Income'].fillna(median_income)

print(f"Filled Age with median: {median_age}")
print(f"Filled Income with median: {median_income}")

# Fill Satisfaction (numeric rating) with median
median_satisfaction = df_fill['Satisfaction'].median()
df_fill['Satisfaction'] = df_fill['Satisfaction'].fillna(median_satisfaction)
print(f"Filled Satisfaction with median: {median_satisfaction}")

# Fill categorical columns
mode_education = df_fill['Education'].mode()[0]
df_fill['Education'] = df_fill['Education'].fillna(mode_education)
print(f"Filled Education with mode: {mode_education}")

df_fill['City'] = df_fill['City'].fillna('Unknown')
print("Filled City with: 'Unknown'")

# Verify no missing values
print(f"\nMissing values after filling: {df_fill.isnull().sum().sum()}")
print(f"Shape preserved: {df_fill.shape}")
```

**Expected output:**
```
Filled Age with median: 31.0
Filled Income with median: 50500.0
Filled Satisfaction with median: 4.0
Filled Education with mode: Bachelor
Filled City with: 'Unknown'

Missing values after filling: 0
Shape preserved: (10, 6)
```

**Key points:**
- "Median for numeric—not affected by outliers"
- "Mode or constant for categorical—makes sense for text data"
- "All rows preserved—no data lost"

---

### Section 4: Comparing Strategies (1:35-1:50) • 15 seconds

**What to say:**
> "Comparing both strategies: dropping lost 50% of rows but kept clean data. Filling preserved all rows but introduced estimates. The best approach? A hybrid: drop rows with missing critical data, then fill non-critical columns."

**What to show:**
```python
# Hybrid approach
df_hybrid = df.copy()

# Step 1: Drop rows with missing critical columns
df_hybrid = df_hybrid.dropna(subset=['Age', 'Income'])

# Step 2: Fill remaining missing values
df_hybrid['Education'] = df_hybrid['Education'].fillna(df_hybrid['Education'].mode()[0])
df_hybrid['Satisfaction'] = df_hybrid['Satisfaction'].fillna(df_hybrid['Satisfaction'].median())
df_hybrid['City'] = df_hybrid['City'].fillna('Unknown')

print("HYBRID STRATEGY:")
print(f"Shape: {df_hybrid.shape}")
print(f"Missing values: {df_hybrid.isnull().sum().sum()}")
print(f"Data lost: {len(df) - len(df_hybrid)} rows ({((len(df) - len(df_hybrid)) / len(df) * 100):.1f}%)")
```

**Expected output:**
```
HYBRID STRATEGY:
Shape: (5, 6)
Missing values: 0
Data lost: 5 rows (50.0%)
```

**Key point:** "Hybrid strategy balances quality and completeness."

---

### Wrap-Up (1:50-2:00) • 10 seconds

**What to say:**
> "Key takeaways: always inspect missing data first, use median for numeric and mode or constant for categorical, and choose strategy based on context—not convenience. Handling missing data responsibly is critical for reliable analysis. Thanks for watching!"

**What to show:**
- Summary points on screen OR final notebook cell
- Professional conclusion

---

## TROUBLESHOOTING GUIDE

### Problem 1: "Mode returns empty series"

**Symptom:** Error when calling `.mode()[0]`

**Cause:** All values in column are missing

**Solution:**
```python
# Check if mode exists before using
if len(df['Column'].mode()) > 0:
    mode_val = df['Column'].mode()[0]
else:
    mode_val = 'Unknown'  # Fallback
```

---

### Problem 2: "Dropna removes all rows"

**Symptom:** DataFrame becomes empty after `dropna()`

**Cause:** Every row has at least one missing value

**Solution:**
```python
# Use subset to target specific columns
df = df.dropna(subset=['CriticalColumn1', 'CriticalColumn2'])

# OR use thresh to allow some missing
df = df.dropna(thresh=len(df.columns) - 2)  # Allow max 2 missing
```

---

### Problem 3: "Median/mean returns NaN"

**Symptom:** Filling with median still leaves NaN values

**Cause:** Entire column is missing

**Solution:**
```python
# Check if column has any non-null values
if df['Column'].notna().any():
    median_val = df['Column'].median()
else:
    median_val = 0  # Or appropriate default
```

---

### Problem 4: "Filled categorical with numeric value"

**Symptom:** Categories show numbers like "2.5" or "3.7"

**Cause:** Used mean/median on categorical data

**Solution:**
```python
# For categorical data, ALWAYS use:
# - mode() for most common value
# - Constant string like 'Unknown'
df['Category'] = df['Category'].fillna(df['Category'].mode()[0])
# OR
df['Category'] = df['Category'].fillna('Unknown')
```

---

### Problem 5: "Lost too much data after dropping"

**Symptom:** >50% of rows removed

**Cause:** Too aggressive dropping strategy

**Solution:**
```python
# Check data loss before committing
original_rows = len(df)
df_after = df.dropna()
loss_pct = ((original_rows - len(df_after)) / original_rows) * 100

if loss_pct > 30:
    print(f"WARNING: {loss_pct:.1f}% data loss - consider filling instead")
    # Use hybrid approach instead
```

---

## CODE TEMPLATE FOR VIDEO

```python
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/survey_data.csv')

# 1. DETECT MISSING VALUES
print("===== DETECTING MISSING VALUES =====")
print(df.isnull().sum())
print("\nPercentage missing:")
print((df.isnull().sum() / len(df)) * 100)

# 2. DROP STRATEGY
print("\n===== DROP STRATEGY =====")
df_drop = df.dropna(subset=['Age', 'Income'])
print(f"Original: {df.shape}, After drop: {df_drop.shape}")

# 3. FILL STRATEGY
print("\n===== FILL STRATEGY =====")
df_fill = df.copy()

# Numeric: use median
df_fill['Age'] = df_fill['Age'].fillna(df_fill['Age'].median())
df_fill['Income'] = df_fill['Income'].fillna(df_fill['Income'].median())
df_fill['Satisfaction'] = df_fill['Satisfaction'].fillna(df_fill['Satisfaction'].median())

# Categorical: use mode or constant
df_fill['Education'] = df_fill['Education'].fillna(df_fill['Education'].mode()[0])
df_fill['City'] = df_fill['City'].fillna('Unknown')

print(f"Original: {df.shape}, After fill: {df_fill.shape}")
print(f"Missing after fill: {df_fill.isnull().sum().sum()}")

# 4. HYBRID APPROACH
print("\n===== HYBRID STRATEGY =====")
df_hybrid = df.copy()
df_hybrid = df_hybrid.dropna(subset=['Age', 'Income'])  # Drop critical
df_hybrid['Education'] = df_hybrid['Education'].fillna(df_hybrid['Education'].mode()[0])
df_hybrid['Satisfaction'] = df_hybrid['Satisfaction'].fillna(df_hybrid['Satisfaction'].median())
df_hybrid['City'] = df_hybrid['City'].fillna('Unknown')

print(f"Original: {df.shape}, Hybrid: {df_hybrid.shape}")
print(f"Missing: {df_hybrid.isnull().sum().sum()}")

# 5. COMPARISON
print("\n===== STRATEGY COMPARISON =====")
print(f"Drop only: {df_drop.shape} - {len(df) - len(df_drop)} rows lost")
print(f"Fill only: {df_fill.shape} - 0 rows lost, {(df.isnull().sum().sum())} values estimated")
print(f"Hybrid: {df_hybrid.shape} - {len(df) - len(df_hybrid)} rows lost, {(df.isnull().sum().sum() - df_hybrid.isnull().sum().sum())} values filled")
```

---

## EXPECTED DEMONSTRATION FLOW

1. **Show the problem** (10 sec)
   - Load data, show missing values exist
   
2. **Demonstrate drop** (25 sec)
   - Show aggressive approach (loses too much)
   - Show targeted approach (better)
   
3. **Demonstrate fill** (40 sec)
   - Fill numeric with median
   - Fill categorical with mode/constant
   - Show all missing values handled
   
4. **Compare strategies** (15 sec)
   - Show hybrid approach
   - Explain trade-offs
   
5. **Conclude** (10 sec)
   - Key takeaways
   - Professional sign-off

---

## QUALITY CHECKLIST

Before submitting your video, verify:

- [ ] Video is **exactly 2 minutes** (±5 seconds acceptable)
- [ ] All **5 required operations** demonstrated
- [ ] Code is **visible and readable** on screen
- [ ] Output is **shown for each operation**
- [ ] Explanation is **clear and audible**
- [ ] You explained **WHY** you chose each strategy
- [ ] You showed **shape changes** (before/after)
- [ ] You demonstrated **hybrid approach**
- [ ] Video has **clear audio** (no background noise)
- [ ] You appear **confident and professional**

---

## COMMON MISTAKES TO AVOID IN VIDEO

❌ **Don't:**
- Skip inspecting missing data first
- Use `dropna()` without parameters (too aggressive)
- Fill categorical with mean/median (creates nonsense)
- Fail to show output of each operation
- Forget to compare shapes before/after
- Use mean instead of median for numeric data
- Not explain WHY you chose each strategy

✅ **Do:**
- Always inspect with `isnull().sum()` first
- Use targeted `dropna(subset=[...])` for critical columns
- Use median for numeric, mode/constant for categorical
- Show shape changes after each operation
- Explain trade-offs (drop = lose data, fill = introduce assumptions)
- Use hybrid approach when possible
- Justify each decision based on data context

---

## POST-RECORDING VERIFICATION

After recording, watch your video and answer:

1. ✅ Did I demonstrate detecting missing values with `isnull().sum()`?
2. ✅ Did I show dropping rows using `dropna()` (preferably with `subset`)?
3. ✅ Did I fill numeric values with median using `fillna()`?
4. ✅ Did I fill categorical values with mode or constant?
5. ✅ Did I compare strategies and show the hybrid approach?
6. ✅ Did I explain why I chose each strategy?
7. ✅ Is my audio clear and professional?
8. ✅ Is my code visible and outputs shown?

**If all checked ✅, submit your video. If any ❌, record again.**

---

## KEY MESSAGES TO EMPHASIZE

### Message 1: "Inspect First"
> "Always use `isnull().sum()` to understand your missing data before deciding how to handle it."

### Message 2: "Choose Based on Context"
> "Don't drop or fill automatically—understand what your data represents and choose accordingly."

### Message 3: "Median for Numeric"
> "For numeric data, median is better than mean because it's not affected by outliers."

### Message 4: "Mode or Constant for Categorical"
> "Categorical data needs mode (most common) or a constant like 'Unknown'—never use mean!"

### Message 5: "Hybrid Approach"
> "The best strategy is often hybrid: drop rows with mission-critical missing data, then fill the rest thoughtfully."

### Message 6: "Verify After Cleaning"
> "Always check `isnull().sum().sum()` after cleaning to ensure all missing values are handled."

---

## TIMING BREAKDOWN (Detailed)

| Section | Time | Content | Words (approx) |
|---------|------|---------|----------------|
| Intro | 0:00-0:10 | Name, milestone, overview | ~25 words |
| Detect | 0:10-0:30 | Load data, show missing values | ~50 words |
| Drop | 0:30-0:55 | Show dropna, targeted approach | ~65 words |
| Fill | 0:55-1:35 | Fill numeric and categorical | ~100 words |
| Compare | 1:35-1:50 | Hybrid strategy, comparison | ~40 words |
| Wrap-up | 1:50-2:00 | Key takeaways, sign-off | ~30 words |
| **Total** | **2:00** | | **~310 words** |

**Speaking pace:** ~155 words per minute (conversational, clear)

---

## SUCCESS METRICS

Your video is successful if:

1. **Completeness:** All 5 required demonstrations included
2. **Clarity:** Viewer can follow and understand each step
3. **Justification:** You explained WHY you chose each strategy
4. **Comparison:** You showed trade-offs between drop and fill
5. **Professionalism:** Clear audio, visible code, confident delivery
6. **Timing:** 2 minutes (±10 seconds acceptable)

---

## FINAL CHECKLIST

- [ ] Recorded video following this guide
- [ ] Video is 2 minutes long
- [ ] All 5 operations demonstrated
- [ ] Code and output visible
- [ ] Explained WHY for each strategy
- [ ] Showed hybrid approach
- [ ] Audio is clear
- [ ] Uploaded video to course platform
- [ ] Submitted milestone for review

**Ready to record? Follow this guide, stay within 2 minutes, and you'll ace Milestone 4.34!**
