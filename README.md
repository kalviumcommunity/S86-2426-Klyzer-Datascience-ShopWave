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

#### Current Observation (from this workspace shell)

```text
conda : The term 'conda' is not recognized as the name of a cmdlet...
```

This indicates Conda is either not installed in this machine context or not initialized on `PATH` for the current terminal profile.

### 4) Jupyter Verification

Run the following in terminal:

```powershell
jupyter --version
jupyter notebook
# or
jupyter lab
```

Inside Jupyter, run a test cell:

```python
print("Jupyter kernel is working")
```

#### Current Observation (from this workspace shell)

```text
jupyter : The term 'jupyter' is not recognized as the name of a cmdlet...
```

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

- [x] Python verified
- [ ] Conda verified in active shell
- [ ] Jupyter verified in active shell
- [ ] PR link attached
- [ ] Video link attached