# Data Organization Guide

## Understanding the Data Lifecycle in Data Science Projects

This guide explains the principles of proper data organization across its lifecycle—from raw inputs to processed datasets and final outputs.

---

## 🎯 Core Principle: Separation of Data Stages

**Data flows in ONE direction:**

```
RAW DATA → PROCESSED DATA → OUTPUT ARTIFACTS
(read-only)   (reproducible)    (final results)
```

**Never mix these stages. Never flow backwards.**

---

## 📁 The Three Data Stages

### 1. Raw Data (`data/raw/`)

**What it is:**
- Original, untouched source data
- Data exactly as received from source (API, file, database, survey, etc.)
- The "source of truth" for your project

**Key Rules:**

✅ **DO:**
- Store data exactly as received
- Treat as **READ-ONLY** (never modify)
- Keep original file names when possible
- Document data source and collection date
- Back up raw data securely

❌ **DON'T:**
- Clean or transform raw data files
- Overwrite raw data with processed versions
- Delete raw data after processing
- Edit values "just this once"
- Save outputs here

**Why it matters:**
- If you corrupt raw data, you lose your source of truth
- Reproducibility requires returning to original data
- Audit trails depend on intact raw data

**Example files:**
```
data/raw/
  ├── sample_sales.csv          ← Downloaded from system
  ├── customer_feedback.json    ← API response saved
  └── sensor_readings.xlsx      ← Exported from device
```

---

### 2. Processed Data (`data/processed/`)

**What it is:**
- Cleaned, transformed, or filtered versions of raw data
- Intermediate datasets created by processing scripts
- Data ready for analysis or modeling

**Key Rules:**

✅ **DO:**
- Save cleaned/transformed datasets here
- Use descriptive names indicating processing stage
- Include date or version in filename if helpful
- Ensure these files can be recreated from raw data + scripts
- Document processing steps in notebooks/scripts

❌ **DON'T:**
- Mix processed files with raw data
- Save final outputs (plots, reports) here
- Overwrite processed files without version control
- Create processed data manually (always use scripts)

**Why it matters:**
- Separates derived data from source data
- Supports traceability (you know what was transformed)
- Enables reproducibility (re-run scripts to recreate)
- Prevents confusion about data lineage

**Example files:**
```
data/processed/
  ├── sample_sales_cleaned.csv       ← Cleaned version of raw sales
  ├── customer_segments.csv          ← Derived from analysis
  └── sensor_readings_normalized.csv ← Transformed raw data
```

---

### 3. Output Artifacts (`outputs/`)

**What it is:**
- Final or intermediate results of analysis
- Visualizations, reports, models, statistics
- Products to be shared or presented

**Organized by type:**
- `outputs/figures/` - Plots, charts, graphs
- `outputs/reports/` - Summary tables, statistical reports
- `outputs/models/` - Trained ML models (if applicable)

**Key Rules:**

✅ **DO:**
- Save all results to outputs folder
- Use clear, descriptive filenames
- Organize by type (figures, reports, models)
- Keep outputs separate from data
- Version outputs if producing multiple iterations

❌ **DON'T:**
- Save outputs in data/raw/ or data/processed/
- Mix different output types in one folder
- Use generic names like "plot.png" or "report.csv"
- Save intermediate processing files here

**Why it matters:**
- Easy to locate results for presentations
- Clear distinction between data and results
- Prevents outputs from contaminating data folders
- Makes sharing results straightforward

**Example files:**
```
outputs/
  ├── figures/
  │   ├── top_customers.png
  │   ├── sales_trend_2024.png
  │   └── correlation_heatmap.png
  └── reports/
      ├── sales_summary_statistics.csv
      ├── monthly_revenue_report.xlsx
      └── customer_analysis.pdf
```

---

## ⚠️ Common Data Contamination Risks

### Risk 1: Overwriting Raw Data

**The Problem:**
```python
# ❌ BAD - Overwrites raw data!
df = pd.read_csv('data/raw/sales.csv')
df = df.dropna()  # Clean data
df.to_csv('data/raw/sales.csv')  # OVERWRITES ORIGINAL!
```

**The Solution:**
```python
# ✅ GOOD - Saves to processed folder
df = pd.read_csv('data/raw/sales.csv')
df = df.dropna()
df.to_csv('data/processed/sales_cleaned.csv')  # Safe!
```

**Consequence if ignored:**
- Original data is lost forever
- Can't reproduce results from true source
- Audit trail is broken

---

### Risk 2: Mixing Data Stages

**The Problem:**
```
data/
  ├── sales.csv              ← Is this raw or processed?
  ├── sales_v2.csv           ← What's the difference?
  ├── sales_final.csv        ← Which one is actually final?
  └── monthly_report.csv     ← Is this data or output?
```

**The Solution:**
```
data/
  ├── raw/
  │   └── sales.csv          ← Clear: this is raw
  ├── processed/
  │   └── sales_cleaned.csv  ← Clear: this is cleaned
outputs/
  └── reports/
      └── monthly_report.csv ← Clear: this is output
```

**Consequence if ignored:**
- Confusion about which file to use
- Risk of using wrong version of data
- Can't trace data lineage

---

### Risk 3: Circular Dependencies

**The Problem:**
```python
# ❌ BAD - Creates circular logic!
# Script 1: Uses processed data to update raw data
df_raw = pd.read_csv('data/raw/sales.csv')
df_processed = pd.read_csv('data/processed/sales_cleaned.csv')
df_raw = df_raw.merge(df_processed, on='id')  # Mixing!
df_raw.to_csv('data/raw/sales.csv')  # Writes back to raw!
```

**The Solution:**
```python
# ✅ GOOD - Clear one-directional flow
df_raw = pd.read_csv('data/raw/sales.csv')  # Read raw
df_cleaned = clean_data(df_raw)             # Process
df_cleaned.to_csv('data/processed/sales_cleaned.csv')  # Save processed
```

**Consequence if ignored:**
- Can't reproduce results
- Data becomes corrupted over time
- Source of truth is lost

---

### Risk 4: Saving Outputs in Data Folders

**The Problem:**
```
data/
  ├── sales.csv              ← Data
  ├── sales_plot.png         ← Output! Doesn't belong here!
  └── summary_stats.csv      ← Output! Doesn't belong here!
```

**The Solution:**
```
data/
  └── sales.csv              ← Only data
outputs/
  ├── figures/
  │   └── sales_plot.png     ← Visualization output
  └── reports/
      └── summary_stats.csv  ← Report output
```

**Consequence if ignored:**
- Data folders become cluttered
- Hard to find actual data vs results
- Confusing for collaborators

---

## ✅ Best Practices Checklist

### When Starting a Project:

- [ ] Create separate folders: `data/raw/`, `data/processed/`, `outputs/`
- [ ] Add README files to each folder explaining purpose
- [ ] Document data sources and collection methods

### When Loading Data:

- [ ] Place original data in `data/raw/` exactly as received
- [ ] Never edit raw data files manually
- [ ] Load raw data as read-only in scripts

### When Processing Data:

- [ ] Read from `data/raw/` only
- [ ] Save results to `data/processed/`
- [ ] Use descriptive filenames indicating processing stage
- [ ] Document processing steps in notebooks/scripts

### When Creating Outputs:

- [ ] Read from `data/processed/` (not raw)
- [ ] Save visualizations to `outputs/figures/`
- [ ] Save reports/statistics to `outputs/reports/`
- [ ] Use clear, descriptive filenames

### When Sharing Work:

- [ ] Ensure raw data is intact and documented
- [ ] Include processing scripts to recreate processed data
- [ ] Package outputs separately for presentation
- [ ] Provide clear README documenting data flow

---

## 🔄 Example Workflow

### Complete Data Lifecycle Example:

```python
# Step 1: Load Raw Data (Read-Only)
import pandas as pd

df_raw = pd.read_csv('data/raw/sample_sales.csv')
print(f"Loaded {len(df_raw)} raw records")

# Step 2: Process Data
df_cleaned = df_raw.dropna()  # Remove missing values
df_cleaned = df_cleaned[df_cleaned['quantity'] > 0]  # Filter invalid

# Step 3: Save Processed Data
df_cleaned.to_csv('data/processed/sample_sales_cleaned.csv', index=False)
print("✓ Saved cleaned data to processed folder")

# Step 4: Analyze Processed Data
total_revenue = df_cleaned['total_amount'].sum()
top_customers = df_cleaned.groupby('customer_id')['total_amount'].sum().nlargest(5)

# Step 5: Generate Outputs
import matplotlib.pyplot as plt

# Save visualization
plt.figure(figsize=(10, 6))
plt.bar(top_customers.index.astype(str), top_customers.values)
plt.xlabel('Customer ID')
plt.ylabel('Total Purchase Amount')
plt.title('Top 5 Customers')
plt.savefig('outputs/figures/top_customers.png')
print("✓ Saved visualization to outputs/figures/")

# Save report
summary = df_cleaned.describe()
summary.to_csv('outputs/reports/sales_summary.csv')
print("✓ Saved report to outputs/reports/")
```

**Data flow:**
```
data/raw/sample_sales.csv
       ↓ (load, clean, filter)
data/processed/sample_sales_cleaned.csv
       ↓ (analyze, visualize)
outputs/figures/top_customers.png
outputs/reports/sales_summary.csv
```

---

## 🎓 Key Takeaways

1. **Raw data is sacred** - Never modify. Always read-only.

2. **Processed data is reproducible** - Can be recreated from raw data + scripts.

3. **Outputs are artifacts** - Final results, clearly separated from data.

4. **Data flows one direction** - raw → processed → outputs. Never backwards.

5. **Separation prevents corruption** - Protects source of truth and enables reproducibility.

6. **Clear organization builds trust** - Others (and future you) can understand and verify your work.

---

## 📚 Summary

| Stage | Purpose | Rules | Can Delete? |
|-------|---------|-------|-------------|
| **Raw Data** | Original source | Read-only, never modify | ❌ NO - Keep forever |
| **Processed Data** | Cleaned/transformed | Derived from raw | ✅ YES - Can recreate |
| **Outputs** | Final results | Generated from processed | ✅ YES - Can recreate |

**Follow these principles, and your Data Science work will remain clean, trustworthy, and reproducible.** ✅
