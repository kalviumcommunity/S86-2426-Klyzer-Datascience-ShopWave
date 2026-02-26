# Milestone 4.12 Quick Guide: Data Organization & Lifecycle

## Assignment: Organizing Raw Data, Processed Data, and Output Artifacts

**Goal:** Demonstrate clear separation between raw, processed, and output data stages to ensure reproducibility and prevent data corruption.

---

## ✅ Checklist Before Recording Video

### 1. Folder Structure Ready

- ✅ `data/raw/` exists with sample data
- ✅ `data/processed/` exists with cleaned data
- ✅ `outputs/figures/` exists with visualizations
- ✅ `outputs/reports/` exists with analytical outputs
- ✅ Each folder has README explaining its purpose

### 2. Data Lifecycle Demonstrated

- ✅ Raw data never modified directly
- ✅ Processing script reads from raw, writes to processed
- ✅ Analysis reads from processed, writes to outputs
- ✅ One-directional flow: raw → processed → outputs

### 3. Examples Ready

- ✅ `data_lifecycle_demo.ipynb` - Shows proper data organization
- ✅ Sample data files in correct locations
- ✅ Clear naming conventions used

### 4. Documentation Complete

- ✅ README files explain each folder's purpose
- ✅ DATA_ORGANIZATION_GUIDE.md explains principles
- ✅ Examples of what NOT to do documented

---

## 🎥 Video Script (~2 Minutes)

### Opening (15 seconds)

> "Hi, I'm demonstrating Milestone 4.12: Organizing Raw Data, Processed Data, and Output Artifacts. This milestone focuses on proper data lifecycle management to ensure reproducibility."

### Section 1: Raw Data (25 seconds)

**Show:** `data/raw/` folder

> "First, the raw data folder. This contains original, untouched data files like `sample_sales.csv`. 
> 
> Key principle: NEVER modify raw data. It's read-only. Think of it as evidence that must be preserved.
>
> Notice the README warns against editing these files directly."

### Section 2: Processed Data (25 seconds)

**Show:** `data/processed/` folder

> "Next, processed data. This contains cleaned and transformed datasets like `sample_sales_cleaned.csv`.
>
> These files are DERIVED from raw data through processing scripts. They can be recreated anytime.
>
> We keep them separate to maintain traceability—we always know the source."

### Section 3: Output Artifacts (25 seconds)

**Show:** `outputs/figures/` and `outputs/reports/` folders

> "Third, output artifacts. These are final results: visualizations in `figures/` and reports in `reports/`.
>
> These are created FROM processed data, not mixed with input data.
>
> Clear separation makes it easy to find results and share them."

### Section 4: Data Flow Demo (30 seconds)

**Show:** `data_lifecycle_demo.ipynb` notebook

> "Here's the complete workflow in action:
>
> 1. Load raw data (read-only)
> 2. Clean and save to processed folder
> 3. Analyze processed data
> 4. Generate outputs to appropriate folders
>
> Notice the one-directional flow: raw → processed → outputs. No backwards contamination."

### Section 5: Why This Matters (15 seconds)

**Show:** Documentation or project structure

> "This separation prevents data corruption, enables reproducibility, and maintains audit trails.
>
> If raw data is overwritten, you lose your source of truth. If stages are mixed, results can't be traced.
>
> This is professional Data Science practice."

### Closing (10 seconds)

> "This completes Milestone 4.12. All data stages are clearly separated, following best practices for reproducible data workflows. Thank you!"

---

## 🎯 Key Points to Emphasize

### Must Mention:

1. **Raw data is read-only** - Never modified
2. **Processed data is derived** - Can be recreated
3. **Outputs are final results** - Clearly separated
4. **One-directional flow** - raw → processed → outputs
5. **Prevents contamination** - Source data protected

### Show in Video:

- ✅ All three folder types
- ✅ README files explaining each
- ✅ Working notebook demonstrating workflow
- ✅ Sample files in correct locations
- ✅ Clear naming conventions

---

## 📋 After Recording

### Submission Checklist:

- [ ] Video is ~2 minutes long
- [ ] Video shows all data folders clearly
- [ ] Video explains separation rationale
- [ ] Screen is clearly visible
- [ ] Audio is clear
- [ ] Video uploaded and link obtained
- [ ] Pull Request created (if required)
- [ ] Video link submitted as instructed

---

## 🚨 Common Mistakes to Avoid

### In Video:

- ❌ Don't just show folders—explain WHY they're separated
- ❌ Don't skip the "read-only raw data" principle
- ❌ Don't forget to show the data flow direction
- ❌ Don't rush—2 minutes is enough to be thorough
- ❌ Don't forget to show example files in each folder

### In Project:

- ❌ Never save processed data back to raw/
- ❌ Never save outputs in data/processed/
- ❌ Never modify raw data files directly
- ❌ Never mix input and output in the same folder

---

## 📚 Files Involved in This Milestone

### Existing Files:

- `data/raw/sample_sales.csv` - Raw data example
- `data/raw/README.md` - Raw data rules
- `data/processed/sample_sales_cleaned.csv` - Processed example
- `data/processed/README.md` - Processed data rules
- `outputs/figures/top_customers.png` - Visualization example
- `outputs/reports/sales_summary_statistics.csv` - Report example
- `outputs/README.md` - Output folder rules
- `structure_demo.ipynb` - Working demonstration

### New Files:

- `MILESTONE_4_12_QUICK_GUIDE.md` - This guide
- `DATA_ORGANIZATION_GUIDE.md` - Detailed principles
- `data_lifecycle_demo.ipynb` - Focused data lifecycle demo

---

## 💡 Pro Tips

### For Better Understanding:

1. **Think of raw data as evidence** - Would you modify evidence? No!
2. **Processed data is reproducible** - If lost, regenerate from raw
3. **Outputs are artifacts** - They showcase your results
4. **Data flows one direction** - Like a river, never backwards

### For the Video:

1. **Practice once** before recording final version
2. **Use clear terminology** - "raw", "processed", "outputs"
3. **Show file contents briefly** - Open a data file or two
4. **Explain consequences** - What happens if data is mixed?
5. **Keep energy positive** - You're demonstrating expertise!

---

## ✅ Success Criteria

You've successfully completed Milestone 4.12 when:

- ✅ All data stages are clearly separated in folders
- ✅ Raw data is never modified in workflows
- ✅ Processed data is properly derived and stored
- ✅ Outputs are in appropriate locations
- ✅ Data flow is one-directional and documented
- ✅ Video clearly explains the organization and rationale
- ✅ Work is submitted correctly

---

**You're ready to record! Follow the script, keep it clear and concise, and show your professional data organization skills.** 🎬
