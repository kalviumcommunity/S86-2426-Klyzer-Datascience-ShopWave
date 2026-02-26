# Milestone 4.13 Quick Guide: Creating and Running Your First Python Script

## What You'll Demonstrate

Show that you can create and run a standalone Python script for a simple data task, then explain the output and why scripts are useful.

---

## Files for This Milestone

- `src/first_data_analysis_script.py` - Standalone script with basic data logic
- `MILESTONE_4_13_QUICK_GUIDE.md` - This checklist and recording guide

---

## What This Script Does

The script demonstrates top-to-bottom execution with simple sample data.

It:
- Defines a small list of daily sales values
- Calculates total, count, average, highest, and lowest values
- Prints results clearly in terminal output
- Uses `if __name__ == "__main__":` to run as a script

---

## Run the Script

From the project root folder:

```powershell
python src/first_data_analysis_script.py
```

If `python` does not work on your machine, use your full interpreter path:

```powershell
C:/Users/kisho/OneDrive/Desktop/new35/.venv/Scripts/python.exe src/first_data_analysis_script.py
```

Expected output summary:
- Header line confirming script start
- Input sales list
- Calculated metrics (days, total, average, max, min)
- Final "completed successfully" message

---

## Script vs Notebook (Key Difference)

### Script (`.py`)
- Runs from top to bottom each time
- No persistent state between runs
- Best for repeatable tasks and automation
- Easy to schedule and reuse

### Notebook (`.ipynb`)
- Interactive and exploratory
- Cells can run out of order
- Kernel state can persist across cell runs
- Best for experimentation and storytelling

Use notebooks to explore, then move stable logic into scripts.

---

## Basic Debugging Checklist

If script execution fails:

1. Confirm you are in the project folder
2. Confirm file path is correct: `src/first_data_analysis_script.py`
3. Check Python is available:
   ```powershell
   python --version
   ```
4. Read the error line and fix syntax/typos
5. Re-run the script after each fix

---

## Video Recording Checklist (~2 Minutes)

### Part 1: Show the Script File (25 sec)
- [ ] Open `src/first_data_analysis_script.py`
- [ ] Briefly explain the sections (`analyze_daily_sales`, `main`, script entry point)
- [ ] Mention that this is standalone Python (not notebook cells)

### Part 2: Run the Script (30 sec)
- [ ] Open terminal in project root
- [ ] Run: `python src/first_data_analysis_script.py`
- [ ] If needed, run with full interpreter path
- [ ] Show that it executes successfully

### Part 3: Explain Output (35 sec)
- [ ] Point out input list
- [ ] Explain total and average values
- [ ] Explain highest/lowest values
- [ ] Confirm top-to-bottom execution completed

### Part 4: Why Scripts Matter (30 sec)
- [ ] "Scripts are repeatable and reusable"
- [ ] "Scripts are better for automation than notebooks"
- [ ] "Scripts reduce confusion from interactive kernel state"
- [ ] "Notebooks are for exploration; scripts are for stable workflows"

---

## Suggested 2-Minute Script

"In this milestone, I created my first standalone Python script for data analysis. The file is in `src/first_data_analysis_script.py`. It uses simple sample sales data and calculates total sales, average sales, highest, and lowest values.

Now I’ll run it from the terminal using `python src/first_data_analysis_script.py`. The output shows the input data, then computed metrics, then a completion message. This confirms the script runs end-to-end from top to bottom.

This is different from notebooks. Notebooks are interactive and great for exploration, but scripts are better for repeatable and automation-friendly workflows. That’s why moving logic from notebooks to scripts is an important Data Science skill." 

---

## Submission Checklist

- [ ] Script file created in `src/`
- [ ] Script runs successfully from terminal
- [ ] Output understood and explained
- [ ] Differences between scripts and notebooks explained
- [ ] ~2 minute video recorded and link ready
