# Milestone 4.7: Jupyter Notebook Launch Guide

## ✓ Setup Complete

Your environment is ready:
- ✓ Conda installed (version 25.11.0)
- ✓ Jupyter Notebook installed
- ✓ Test notebook created in `notebooks/` folder

---

## Step-by-Step Instructions

### Step 1: Launch Jupyter Notebook from Terminal

**Open your terminal (PowerShell or Command Prompt) and run:**

```powershell
cd D:\Data-Science\S86-2426-Klyzer-Datascience-ShopWave
jupyter notebook
```

**What happens:**
- Jupyter will start a local server
- Your default web browser will open automatically
- You'll see the Jupyter Home interface
- The terminal will show server logs (keep it open!)

**Important:** Launch Jupyter from your project folder so all your files are accessible.

---

### Step 2: Understanding the Jupyter Home Interface

When Jupyter opens in your browser, you'll see:

**Key Elements:**
1. **File/Folder Listing** - Shows all files and folders in your project
2. **Navigation Breadcrumbs** - Shows current location (top of page)
3. **New Button** (top right) - Create new notebooks, folders, or files
4. **Upload Button** - Upload files to current directory
5. **Running Tab** - Shows currently running notebooks
6. **File Checkboxes** - Select files for batch operations (delete, move, etc.)

**File Type Indicators:**
- 📁 Folder icon = Directory
- 📓 Orange notebook icon = Jupyter Notebook (.ipynb)
- 📄 Text icon = Python scripts (.py) or other files

---

### Step 3: Navigate to Your Project Folders

**Practice Navigation:**
1. Look for the `notebooks/` folder in the file list
2. Click on `notebooks/` to enter the directory
3. You'll see `milestone_4_7_test.ipynb` inside
4. Click the "Home" breadcrumb or folder name to go back

**Understanding Your Location:**
- The breadcrumb path shows: `Home > notebooks`
- This maps to: `D:\Data-Science\S86-2426-Klyzer-Datascience-ShopWave\notebooks`

---

### Step 4: Open and Run the Test Notebook

**Open the notebook:**
1. Navigate to the `notebooks/` folder
2. Click on `milestone_4_7_test.ipynb`
3. The notebook opens in a new browser tab

**Run the cells:**
1. Click on the first code cell (starts with "# Test Cell 1")
2. Press **Shift + Enter** to run it
3. You'll see Python version info as output
4. Repeat for all remaining cells

**Expected Results:**
- Each cell runs without errors
- You see output below each code cell
- The last cell shows your current working directory

---

### Step 5: Notebook File Management

**Rename the notebook:**
1. Click "File" menu → "Rename..."
2. Try renaming it to: `my_jupyter_test`
3. Click "Rename" to confirm

**Save your work:**
- Press **Ctrl + S** (Windows) or **Cmd + S** (Mac)
- Or click the save icon (floppy disk)
- Autosave runs every few minutes

**Close safely:**
1. Click "File" menu → "Close and Halt"
2. This stops the kernel and closes the notebook
3. You're back at the Home interface

**Reopen the notebook:**
1. Navigate to `notebooks/` folder again
2. Click on your renamed notebook
3. It opens with all previous content intact

---

### Step 6: Create a New Notebook

**To demonstrate you understand the workflow:**

1. Navigate to the `notebooks/` folder
2. Click "New" → "Python 3" (or "Notebook: Python 3")
3. A new untitled notebook opens
4. Run a simple test:
   ```python
   print("Hello from my new notebook!")
   ```
5. Save and rename it to `navigation_practice`

---

## Video Recording Checklist (~2 minutes)

Record your screen showing:

### Part 1: Launch (30 seconds)
- [ ] Open terminal/command prompt
- [ ] Show the command: `jupyter notebook`
- [ ] Press Enter and wait for browser to open

### Part 2: Home Interface (30 seconds)
- [ ] Point out the file listing area
- [ ] Show the breadcrumb navigation
- [ ] Highlight the "New" button
- [ ] Show folder vs. notebook icons

### Part 3: Navigation (30 seconds)
- [ ] Navigate into the `notebooks/` folder
- [ ] Navigate back out
- [ ] Explain what you're seeing

### Part 4: Notebook Operations (30 seconds)
- [ ] Open `milestone_4_7_test.ipynb`
- [ ] Run at least 2 cells (Shift + Enter)
- [ ] Show the output
- [ ] Save the notebook (Ctrl/Cmd + S)
- [ ] Close and return to Home

**Recording Tips:**
- Use screen recording software (Windows: Xbox Game Bar, OBS Studio, or Loom)
- Speak clearly and concisely
- No need to read everything - just demonstrate confidence
- Keep it around 2 minutes total

---

## Command Reference

**Launch Jupyter:**
```powershell
cd D:\Data-Science\S86-2426-Klyzer-Datascience-ShopWave
jupyter notebook
```

**Stop Jupyter:**
- Press **Ctrl + C** in the terminal twice
- Or close the terminal window

**Check installations:**
```powershell
conda --version
jupyter --version
python --version
```

---

## Common Issues & Solutions

**Issue: Jupyter opens in wrong folder**
- Solution: Always `cd` to your project folder first

**Issue: Kernel not connecting**
- Solution: Wait a few seconds, refresh the browser

**Issue: "Module not found" when importing**
- Solution: Check you're in the correct conda environment
  ```powershell
  conda env list
  conda activate base
  ```

**Issue: Can't find notebook file**
- Solution: Check you're in the right folder (look at breadcrumbs)

---

## Submission Requirements

When submitting Milestone 4.7:

1. **Pull Request (if needed):**
   - Include this `JUPYTER_LAUNCH_GUIDE.md`
   - Include the `notebooks/` folder with your test notebook
   - Include screenshots if required

2. **Video:**
   - Upload to YouTube, Google Drive, or required platform
   - Make sure it's accessible (check sharing settings)
   - Submit the link as instructed

3. **Required Content:**
   - Screen-facing video showing Jupyter operations
   - Approximately 2 minutes duration
   - Clear demonstration of all checklist items

---

## ✅ What You've Learned

By completing this milestone, you can now:
- ✓ Launch Jupyter Notebook from the correct directory
- ✓ Identify and navigate the Jupyter Home interface
- ✓ Navigate folders intentionally and safely
- ✓ Create, open, and run notebooks
- ✓ Manage notebook files (rename, save, close, reopen)
- ✓ Understand where your files are being saved

**You're now ready for data science work!**

---

## Next Steps

After completing this milestone:
1. Keep practicing notebook navigation
2. Always launch Jupyter from your project root
3. Stay organized - use folders for different notebook types
4. Remember: the terminal must stay open while Jupyter runs

Good luck with your assignment! 🚀
