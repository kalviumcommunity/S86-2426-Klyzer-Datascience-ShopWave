# Milestone 4.35: Identifying and Removing Duplicate Records - 2-Minute Video Guide

**Total Time: 2 minutes (120 seconds)**

---

## SUCCESS CRITERIA

Your video must demonstrate **ALL 5 of these operations**:

1. ✅ **Detect Duplicates** using `duplicated()`
2. ✅ **Inspect Duplicate Rows** showing all occurrences
3. ✅ **Remove Duplicates** using `drop_duplicates()`
4. ✅ **Compare Shape** before and after (show rows removed)
5. ✅ **Explain Why** deduplication matters for accurate analysis

**Note:** If any of these 5 are missing, record again.

---

## VIDEO STRUCTURE & TIMING

### Introduction (0:00-0:10) • 10 seconds

**What to say:**
> "Hi, I'm [Your Name]. This is Milestone 4.35—Identifying and Removing Duplicate Records. I'll show you how to detect duplicates, inspect them, remove them safely, and why this matters for accurate data analysis."

**What to show:**
- Milestone title slide or notebook open
- Confident, clear voice

---

### Section 1: Detecting Duplicates (0:10-0:35) • 25 seconds

**What to say:**
> "First, I'll load customer data and check for duplicates using `duplicated()`. This returns True for duplicate rows. I can see we have 5 duplicate rows out of 15 total. Now I'll use `keep=False` to show ALL duplicate rows including the originals, so I can see exactly which customers appear multiple times."

**What to show:**
```python
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/customer_data.csv')
print(f"Total rows: {len(df)}")

# Detect duplicates
n_duplicates = df.duplicated().sum()
print(f"Duplicate rows: {n_duplicates}")

# Show ALL duplicates (including originals)
print("\nAll duplicate records:")
all_dupes = df[df.duplicated(keep=False)]
print(all_dupes.sort_values('CustomerID'))
```

**Expected output:**
```
Total rows: 15
Duplicate rows: 5

All duplicate records:
   CustomerID         Name                  Email        City SignupDate
0        1001   John Smith  john.smith@email.com    New York 2024-01-15
2        1001   John Smith  john.smith@email.com    New York 2024-01-15
11       1001   John Smith  john.smith@email.com    New York 2024-01-15
1        1002 Sarah Johnson       sarah.j@email.com Los Angeles 2024-01-18
5        1002 Sarah Johnson       sarah.j@email.com Los Angeles 2024-01-18
...
```

**Key points:**
- "5 duplicate rows means 5 extra copies"
- "Using keep=False shows the original plus all copies"
- "Customer 1001 appears 3 times—that's problematic!"

---

### Section 2: Removing Duplicates (0:35-1:05) • 30 seconds

**What to say:**
> "Now I'll remove these duplicates using `drop_duplicates()`. By default, it keeps the first occurrence and removes the rest. I can also specify which columns to check—here I'll deduplicate based on CustomerID only, ensuring one record per customer. Let me show the before and after shapes."

**What to show:**
```python
# Before
print("BEFORE deduplication:")
print(f"Shape: {df.shape}")
print(f"Unique customers: {df['CustomerID'].nunique()}")

# Remove duplicates
df_clean = df.drop_duplicates(subset=['CustomerID'], keep='first')

# After
print("\nAFTER deduplication:")
print(f"Shape: {df_clean.shape}")
print(f"Unique customers: {df_clean['CustomerID'].nunique()}")
print(f"Rows removed: {len(df) - len(df_clean)}")

print("\nCleaned data:")
print(df_clean[['CustomerID', 'Name', 'Email']])
```

**Expected output:**
```
BEFORE deduplication:
Shape: (15, 5)
Unique customers: 10

AFTER deduplication:
Shape: (10, 5)
Unique customers: 10
Rows removed: 5

Cleaned data:
   CustomerID            Name                    Email
0        1001      John Smith    john.smith@email.com
1        1002   Sarah Johnson         sarah.j@email.com
3        1003    Mike Williams            mike.w@email.com
...
```

**Key points:**
- "15 rows became 10—removed 5 duplicates"
- "Now have exactly one record per customer"
- "Using subset=['CustomerID'] focuses on business key"

---

### Section 3: Verifying Deduplication (1:05-1:25) • 20 seconds

**What to say:**
> "Always verify your deduplication worked. I'll check if any duplicates remain. Zero duplicates—perfect! Also confirming that the number of rows equals the number of unique CustomerIDs, which proves each customer appears exactly once."

**What to show:**
```python
# Verify no duplicates remain
remaining_dupes = df_clean.duplicated(subset=['CustomerID']).sum()
print(f"Remaining duplicates: {remaining_dupes}")

# Double-check uniqueness
n_rows = len(df_clean)
n_unique = df_clean['CustomerID'].nunique()
print(f"Total rows: {n_rows}")
print(f"Unique CustomerIDs: {n_unique}")

if n_rows == n_unique:
    print("✅ SUCCESS: All CustomerIDs are unique!")
else:
    print("⚠️ WARNING: Duplicates still exist!")
```

**Expected output:**
```
Remaining duplicates: 0
Total rows: 10
Unique CustomerIDs: 10
✅ SUCCESS: All CustomerIDs are unique!
```

**Key point:** "Always verify—don't assume deduplication worked!"

---

### Section 4: Impact on Analysis (1:25-1:50) • 25 seconds

**What to say:**
> "Let me show why this matters. I'll load transaction data with duplicate transaction IDs. If I calculate total revenue with duplicates, I get an inflated number. After removing duplicates, the true revenue is lower. This shows how duplicates corrupt analysis—we were overcounting by almost 30% due to duplicate records!"

**What to show:**
```python
# Load transaction data
txn_df = pd.read_csv('../data/raw/transactions.csv')

# Revenue WITH duplicates
revenue_with_dupes = txn_df['Amount'].sum()
print(f"Revenue with duplicates: ${revenue_with_dupes:,.2f}")

# Remove duplicates
txn_clean = txn_df.drop_duplicates(subset=['TransactionID'])

# Revenue AFTER deduplication
revenue_clean = txn_clean['Amount'].sum()
print(f"Revenue after deduplication: ${revenue_clean:,.2f}")

# Show impact
overcount = revenue_with_dupes - revenue_clean
pct_overcount = (overcount / revenue_clean) * 100
print(f"\nOvercount: ${overcount:,.2f} ({pct_overcount:.1f}%)")
print(f"Rows removed: {len(txn_df) - len(txn_clean)}")
```

**Expected output:**
```
Revenue with duplicates: $4,824.45
Revenue after deduplication: $3,749.46
Overcount: $1,074.99 (28.7%)
Rows removed: 5
```

**Key points:**
- "Duplicates inflated revenue by nearly 29%!"
- "This is why deduplication is critical"
- "Clean data leads to accurate business decisions"

---

### Wrap-Up (1:50-2:00) • 10 seconds

**What to say:**
> "Key takeaways: use `duplicated()` to detect, `drop_duplicates()` to remove, always specify subset for business keys, and verify your results. Duplicate records silently corrupt analysis—deduplication ensures each observation is counted exactly once. Thanks for watching!"

**What to show:**
- Summary points on screen OR final notebook cell
- Professional conclusion

---

## TROUBLESHOOTING GUIDE

### Problem 1: "No duplicates found but data looks wrong"

**Symptom:** `duplicated().sum()` returns 0 but you see repeated values

**Cause:** Checking all columns, but only some columns are duplicate

**Solution:**
```python
# Check specific columns only
df.duplicated(subset=['CustomerID']).sum()
# OR
df.duplicated(subset=['Email']).sum()
```

---

### Problem 2: "Removed too many rows"

**Symptom:** `drop_duplicates()` removed more rows than expected

**Cause:** Used `keep=False` instead of `keep='first'`

**Solution:**
```python
# Keep first occurrence (DEFAULT)
df_clean = df.drop_duplicates(keep='first')

# NOT this (removes ALL duplicates including originals)
# df_clean = df.drop_duplicates(keep=False)
```

---

### Problem 3: "Can't see which rows are duplicates"

**Symptom:** `duplicated()` returns boolean series, hard to inspect

**Cause:** Not using `keep=False` to show all occurrences

**Solution:**
```python
# Show ALL duplicate rows (including originals)
all_duplicates = df[df.duplicated(keep=False)]
print(all_duplicates.sort_values('ID'))
```

---

### Problem 4: "Wrong rows being kept"

**Symptom:** Kept older/newer record when wanted opposite

**Cause:** Used wrong `keep` parameter

**Solution:**
```python
# Keep FIRST occurrence (earliest)
df.drop_duplicates(keep='first')

# Keep LAST occurrence (latest)
df.drop_duplicates(keep='last')

# Remove ALL duplicates (keep none)
df.drop_duplicates(keep=False)
```

---

### Problem 5: "Deduplication didn't work"

**Symptom:** Still see duplicates after `drop_duplicates()`

**Cause:** Forgot to assign result or use `inplace=True`

**Solution:**
```python
# WRONG: Doesn't save result
df.drop_duplicates()

# RIGHT: Assign to new variable
df_clean = df.drop_duplicates()

# OR: Modify in place
df.drop_duplicates(inplace=True)
```

---

## CODE TEMPLATE FOR VIDEO

```python
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/customer_data.csv')

# 1. DETECT DUPLICATES
print("===== DETECTING DUPLICATES =====")
print(f"Total rows: {len(df)}")
print(f"Duplicates: {df.duplicated().sum()}")
print(f"Unique customers: {df['CustomerID'].nunique()}")

# Show duplicates
print("\nAll duplicate records:")
print(df[df.duplicated(keep=False)].sort_values('CustomerID'))

# 2. REMOVE DUPLICATES
print("\n===== REMOVING DUPLICATES =====")
print(f"Before: {df.shape}")

df_clean = df.drop_duplicates(subset=['CustomerID'], keep='first')

print(f"After: {df_clean.shape}")
print(f"Removed: {len(df) - len(df_clean)} rows")

# 3. VERIFY
print("\n===== VERIFICATION =====")
print(f"Remaining duplicates: {df_clean.duplicated(subset=['CustomerID']).sum()}")
if df_clean['CustomerID'].nunique() == len(df_clean):
    print("✅ SUCCESS: All CustomerIDs are unique!")

# 4. IMPACT ANALYSIS
print("\n===== IMPACT ON ANALYSIS =====")
txn_df = pd.read_csv('../data/raw/transactions.csv')
revenue_before = txn_df['Amount'].sum()
txn_clean = txn_df.drop_duplicates(subset=['TransactionID'])
revenue_after = txn_clean['Amount'].sum()

print(f"Revenue with dupes: ${revenue_before:,.2f}")
print(f"Revenue after dedup: ${revenue_after:,.2f}")
print(f"Overcount: ${revenue_before - revenue_after:,.2f}")
print(f"Percentage: {((revenue_before - revenue_after) / revenue_after * 100):.1f}%")
```

---

## EXPECTED DEMONSTRATION FLOW

1. **Load and inspect** (10 sec)
   - Show dataset, mention it may have duplicates
   
2. **Detect duplicates** (25 sec)
   - Use `duplicated()` to count
   - Show all duplicates with `keep=False`
   
3. **Remove duplicates** (30 sec)
   - Use `drop_duplicates(subset=['ID'])`
   - Show shape before/after
   - Explain rows removed
   
4. **Verify results** (20 sec)
   - Check no duplicates remain
   - Confirm uniqueness
   
5. **Show impact** (25 sec)
   - Demonstrate on transaction data
   - Calculate revenue with/without duplicates
   - Show percentage overcount
   
6. **Conclude** (10 sec)
   - Key takeaways
   - Why it matters

---

## QUALITY CHECKLIST

Before submitting your video, verify:

- [ ] Video is **exactly 2 minutes** (±5 seconds acceptable)
- [ ] All **5 required operations** demonstrated
- [ ] Code is **visible and readable** on screen
- [ ] Output is **shown for each operation**
- [ ] Explanation is **clear and audible**
- [ ] You showed **all duplicates** using `keep=False`
- [ ] You showed **shape changes** (before/after)
- [ ] You demonstrated **verification** step
- [ ] You explained **impact on analysis** (revenue example)
- [ ] Video has **clear audio** (no background noise)
- [ ] You appear **confident and professional**

---

## COMMON MISTAKES TO AVOID IN VIDEO

❌ **Don't:**
- Use `duplicated()` without showing the actual duplicate rows
- Remove duplicates without checking subset parameter
- Forget to verify deduplication worked
- Skip showing the impact on analysis
- Use all columns when only key columns matter
- Forget to explain which occurrence is kept (first/last)

✅ **Do:**
- Show duplicates with `keep=False` to see all occurrences
- Use `subset=['KeyColumn']` for business key deduplication
- Verify with `duplicated().sum()` after removal
- Show real impact (e.g., revenue overcount)
- Explain why deduplication matters
- Compare shape before and after

---

## POST-RECORDING VERIFICATION

After recording, watch your video and answer:

1. ✅ Did I detect duplicates with `duplicated()`?
2. ✅ Did I show all duplicate rows (including originals)?
3. ✅ Did I remove duplicates with `drop_duplicates()`?
4. ✅ Did I show shape comparison (before/after)?
5. ✅ Did I verify no duplicates remain?
6. ✅ Did I explain the impact on analysis?
7. ✅ Is my audio clear and professional?
8. ✅ Is my code visible and outputs shown?

**If all checked ✅, submit your video. If any ❌, record again.**

---

## KEY MESSAGES TO EMPHASIZE

### Message 1: "Always Inspect First"
> "Use `duplicated(keep=False)` to see ALL duplicate rows including originals before deciding what to remove."

### Message 2: "Use Subset for Business Keys"
> "Don't check all columns—use `subset=['ID']` to focus on columns that define uniqueness."

### Message 3: "Verify After Removal"
> "Always check that deduplication worked by counting remaining duplicates and confirming uniqueness."

### Message 4: "Duplicates Corrupt Analysis"
> "Duplicate records inflate counts and metrics—we saw revenue overcounted by 29% due to duplicates!"

### Message 5: "Keep First by Default"
> "By default, `keep='first'` preserves the first occurrence—use `keep='last'` if you want the most recent."

### Message 6: "Not All Repeats Are Duplicates"
> "Customer making multiple purchases is NOT a duplicate—same customer record appearing twice IS."

---

## TIMING BREAKDOWN (Detailed)

| Section | Time | Content | Words (approx) |
|---------|------|---------|----------------|
| Intro | 0:00-0:10 | Name, milestone, overview | ~25 words |
| Detect | 0:10-0:35 | Find duplicates, show all occurrences | ~65 words |
| Remove | 0:35-1:05 | Drop duplicates, show before/after | ~75 words |
| Verify | 1:05-1:25 | Check no duplicates remain | ~50 words |
| Impact | 1:25-1:50 | Revenue overcount example | ~65 words |
| Wrap-up | 1:50-2:00 | Key takeaways, sign-off | ~30 words |
| **Total** | **2:00** | | **~310 words** |

**Speaking pace:** ~155 words per minute (conversational, clear)

---

## SUCCESS METRICS

Your video is successful if:

1. **Completeness:** All 5 required demonstrations included
2. **Detection:** Clearly showed how to find duplicates
3. **Inspection:** Showed all duplicate rows (not just marked ones)
4. **Removal:** Used `drop_duplicates()` with appropriate parameters
5. **Verification:** Confirmed no duplicates remain
6. **Impact:** Demonstrated real consequence (revenue inflation)
7. **Timing:** 2 minutes (±10 seconds acceptable)

---

## FINAL CHECKLIST

- [ ] Recorded video following this guide
- [ ] Video is 2 minutes long
- [ ] All 5 operations demonstrated
- [ ] Code and output visible
- [ ] Showed duplicate detection with `duplicated()`
- [ ] Showed inspection with `keep=False`
- [ ] Showed removal with `drop_duplicates(subset=...)`
- [ ] Showed shape before/after comparison
- [ ] Verified deduplication success
- [ ] Explained impact on analysis
- [ ] Audio is clear
- [ ] Uploaded video to course platform
- [ ] Submitted milestone for review

**Ready to record? Follow this guide, demonstrate the impact of duplicates on analysis, and you'll ace Milestone 4.35!**
