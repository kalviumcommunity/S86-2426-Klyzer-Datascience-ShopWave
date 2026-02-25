# S86-2426-Klyzer-Datascience-ShopWave

## Milestone: Python + Conda + Jupyter Verification

This section records environment verification for Data Science sprint readiness.

### 1) Machine Information

- **Operating System:** Windows
- **Python Version:** 3.12.6
- **Environment Target:** Conda `base` (or named sprint env)

### 2) Python Verification

Python is callable and launches successfully from terminal.

#### Commands

```powershell
python --version
py --version
where python
```

#### Output (Captured)

```text
Python 3.12.6
Python 3.12.6
C:\Users\kisho\AppData\Local\Programs\Python\Python312\python.exe
C:\Users\kisho\AppData\Local\Microsoft\WindowsApps\python.exe
```

### 3) Conda Verification

Run the following in terminal:

```powershell
conda --version
conda env list
conda activate base
```

#### Verified Output

```text
conda 25.11.0
```

✅ Conda is installed and accessible.

### 4) Jupyter Verification

Run the following in terminal:

```powershell
jupyter --version
python -m jupyter --version
jupyter notebook
```

Inside Jupyter, run a test cell:

```python
print("Jupyter kernel is working")
```

#### Verified Output

```text
Selected Jupyter core packages...
IPython          : 9.7.0
ipykernel        : 6.31.0
ipywidgets       : 8.1.7
jupyter_client   : 8.6.3
jupyter_core     : 5.8.1
jupyter_server   : 2.16.0
jupyterlab       : 4.4.7
nbclient         : 0.10.2
```

✅ Jupyter Notebook and JupyterLab are installed and ready.

### 5) PR Evidence Checklist

Include all of the following in the PR:

1. `python --version` output
2. `conda --version` output
3. `conda env list` and active environment prompt after `conda activate base`
4. Jupyter notebook/lab launch proof and one successful Python cell output
5. Link to a ~2 minute walkthrough video

### 6) Video Walkthrough Checklist (~2 mins)

- Show terminal: Python version check
- Show terminal: Conda version + environment activation
- Show Jupyter Notebook/Lab running one Python cell
- Show this README verification section
- Briefly explain what was verified and why

### 7) Verification Status

- [x] Python verified (v3.12.6)
- [x] Conda verified (v25.11.0)
- [x] Jupyter verified (JupyterLab 4.4.7, Notebook ready)
- [ ] PR link attached
- [ ] Video link attached

---

## Milestone 4.7: Launching Jupyter Notebook and Understanding the Home Interface

### Objective

Launch Jupyter Notebook correctly and demonstrate understanding of the Home interface, navigation, and notebook management.

### Setup Complete

- ✅ Conda environment verified
- ✅ Jupyter Notebook installed
- ✅ Project folder structure created (`notebooks/`)
- ✅ Test notebook created (`milestone_4_7_test.ipynb`)
- ✅ Launch guide documentation created

### Files Created for This Milestone

1. **`notebooks/milestone_4_7_test.ipynb`** - Test notebook with verification cells
2. **`JUPYTER_LAUNCH_GUIDE.md`** - Complete step-by-step instructions
3. **`MILESTONE_4_7_QUICK_START.md`** - Quick reference commands

### Quick Start

**Launch Jupyter Notebook:**

```powershell
cd D:\Data-Science\S86-2426-Klyzer-Datascience-ShopWave
jupyter notebook
```

**What to do:**
1. Jupyter opens in your browser
2. Navigate to the `notebooks/` folder
3. Open `milestone_4_7_test.ipynb`
4. Run all cells (Shift + Enter)
5. Practice renaming, saving, and reopening notebooks

### Video Recording Requirements

Record a ~2 minute screen capture showing:
- ✅ Launching Jupyter from terminal
- ✅ Navigating the Home interface
- ✅ Opening and running the test notebook
- ✅ Basic file management (save, rename, close, reopen)

### Submission Checklist

- [ ] Launched Jupyter Notebook successfully
- [ ] Navigated folders in Jupyter Home interface
- [ ] Created and ran test notebook
- [ ] Recorded 2-minute walkthrough video
- [ ] Video uploaded and link ready
- [ ] Pull Request created (if required)

### Documentation

For complete instructions, see **[JUPYTER_LAUNCH_GUIDE.md](JUPYTER_LAUNCH_GUIDE.md)**

### Status

**Current Status:** ✅ Setup Complete - Ready for Video Recording

**Next Action:** Launch Jupyter and record your walkthrough video following the guide.