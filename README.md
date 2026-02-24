# S86-2426-Klyzer-Datascience-ShopWave

## Milestone: Local Setup (Python + Anaconda)

This section documents the local machine setup required for the Data Science sprint.

### 1) System Information

- **Operating System:** Windows
- **Python Version:** 3.12.6
- **Anaconda Version:** To be verified after installation (`conda --version`)

### 2) Python Installation Verification

Python is available in terminal and callable from command line.

#### Commands used

```powershell
python --version
py --version
where python
```

#### Output captured

```text
Python 3.12.6
Python 3.12.6
C:\Users\kisho\AppData\Local\Programs\Python\Python312\python.exe
C:\Users\kisho\AppData\Local\Microsoft\WindowsApps\python.exe
```

### 3) Anaconda Installation & Setup

Install Anaconda (Windows) using `winget`:

```powershell
winget search Anaconda3
winget install --id Anaconda.Anaconda3 -e --accept-package-agreements --accept-source-agreements
```

After installation, restart terminal and verify Conda:

```powershell
conda --version
conda info
```

If `conda` is not recognized, initialize shell:

```powershell
& "$HOME\anaconda3\Scripts\conda.exe" init powershell
```

Then close and reopen terminal.

### 4) Environment Validation (Data Science Ready Check)

Use the following commands to validate the environment:

```powershell
conda activate base
python --version
python -c "import sys; print(sys.executable)"
python -c "import numpy, pandas; print('numpy/pandas import OK')"
```

Optional custom environment for sprint work:

```powershell
conda create -n ds-sprint python=3.12 -y
conda activate ds-sprint
python --version
```

### 5) Proof for PR Submission

Include the following in your PR:

1. Terminal screenshot/output of `python --version`
2. Terminal screenshot/output of `conda --version`
3. Terminal screenshot/output of successful environment activation
4. Link to a ~2 minute setup walkthrough video showing:
	- Python version check
	- Conda version check
	- Quick walkthrough of this README section
	- Brief explanation of what was verified

### 6) Current Verification Status (This Machine)

- [x] Python is installed and verified (`3.12.6`)
- [ ] Anaconda/Conda verification pending completion in terminal
- [ ] Final proof screenshots/video to be attached in PR