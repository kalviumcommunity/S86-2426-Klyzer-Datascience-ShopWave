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

---

## Milestone 4.8: Understanding Notebook Cells - Code vs Markdown

### Objective

Demonstrate clear understanding of the difference between Code cells and Markdown cells, and use them intentionally to create readable, professional notebooks.

### Setup Complete

- ✅ Demonstration notebook created (`milestone_4_8_cells.ipynb`)
- ✅ Examples of both Code and Markdown cells included
- ✅ Cell switching demonstrations prepared
- ✅ Quick guide documentation created

### Files Created for This Milestone

1. **`notebooks/milestone_4_8_cells.ipynb`** - Complete demonstration notebook
2. **`MILESTONE_4_8_QUICK_GUIDE.md`** - Video recording guide and shortcuts

### Key Concepts

**Code Cells:**
- Execute Python code
- Show computational output
- Perform operations and calculations
- Should contain logic, not lengthy explanations

**Markdown Cells:**
- Provide explanation and context
- Create structure with headings
- Document reasoning and methodology
- Should contain narrative, not code execution

### Quick Start

**Open the notebook in Jupyter:**

1. Make sure Jupyter is running (see Milestone 4.7)
2. Navigate to `notebooks/` folder
3. Open `milestone_4_8_cells.ipynb`
4. Run cells and observe the difference between types

### Video Recording Requirements

Record a ~2 minute screen capture showing:
- ✅ Demonstrating a Code cell (run it, show output)
- ✅ Demonstrating a Markdown cell (edit and render)
- ✅ Switching between cell types
- ✅ Creating new cells of both types
- ✅ Explaining when to use Code vs Markdown

### Submission Checklist

- [ ] Opened `milestone_4_8_cells.ipynb` in Jupyter
- [ ] Ran all Code cells successfully
- [ ] Demonstrated cell type switching
- [ ] Created new cells (both types)
- [ ] Recorded 2-minute walkthrough video
- [ ] Video uploaded and link ready
- [ ] Pull Request created (if required)

### Documentation

For complete instructions, see **[MILESTONE_4_8_QUICK_GUIDE.md](MILESTONE_4_8_QUICK_GUIDE.md)**

### Status

**Current Status:** ✅ Setup Complete - Ready for Video Recording

**Next Action:** Open the notebook in Jupyter and record your demonstration following the quick guide.

---

## Milestone 4.9: Running, Restarting, and Interrupting Jupyter Kernels

### Objective

Understand how Jupyter kernels work and learn to control them safely for debugging, reproducibility, and maintaining clean notebook state.

### Setup Complete

- ✅ Kernel management demonstration notebook created (`milestone_4_9_kernels.ipynb`)
- ✅ Examples of running, interrupting, and restarting included
- ✅ Long-running and infinite loop exercises prepared
- ✅ Quick guide documentation created

### Files Created for This Milestone

1. **`notebooks/milestone_4_9_kernels.ipynb`** - Complete kernel management demonstration
2. **`MILESTONE_4_9_QUICK_GUIDE.md`** - Video recording guide with detailed script

### Key Concepts

**Jupyter Kernel:**
- The computational engine that executes your code
- Maintains memory and state between cell executions
- Can be in idle (ready) or busy (executing) state

**Running Cells:**
- Executes code and maintains state in kernel memory
- Variables persist until kernel is restarted
- Execution order matters, not cell position

**Interrupting:**
- Stops current execution without clearing memory
- Use for long-running or stuck cells
- Kernel remains responsive afterward

**Restarting:**
- Clears all variables and memory
- Provides a clean slate for testing
- Essential for reproducibility testing

### Quick Start

**Open the notebook in Jupyter:**

1. Make sure Jupyter is running (see Milestone 4.7)
2. Navigate to `notebooks/` folder
3. Open `milestone_4_9_kernels.ipynb`
4. Work through the exercises to practice kernel control

### Video Recording Requirements

Record a ~2 minute screen capture showing:
- ✅ Running cells in sequence (show kernel indicator)
- ✅ Interrupting a long-running cell
- ✅ Restarting the kernel
- ✅ Running all cells after restart
- ✅ Explaining when to use each action

### Key Actions to Demonstrate

**Interrupt:** `Kernel → Interrupt` (or stop button)
- Stops execution, keeps variables in memory

**Restart:** `Kernel → Restart`
- Clears all memory, fresh start

**Restart & Run All:** `Kernel → Restart & Run All`
- Tests complete notebook reproducibility

### Submission Checklist

- [ ] Opened `milestone_4_9_kernels.ipynb` in Jupyter
- [ ] Practiced running cells in sequence
- [ ] Interrupted the countdown cell
- [ ] Restarted the kernel and observed variables cleared
- [ ] Tested "Restart & Run All"
- [ ] Recorded 2-minute walkthrough video
- [ ] Video uploaded and link ready
- [ ] Pull Request created (if required)

### Documentation

For complete instructions, see **[MILESTONE_4_9_QUICK_GUIDE.md](MILESTONE_4_9_QUICK_GUIDE.md)**

### Status

**Current Status:** ✅ Setup Complete - Ready for Video Recording

**Next Action:** Open the notebook in Jupyter and practice kernel management, then record your demonstration following the quick guide.

---

## Milestone 4.10: Writing Markdown for Headings, Lists, and Code Blocks

### Objective

Learn to write clear, professional Markdown documentation in Jupyter Notebooks using proper formatting for headings, lists, inline code, and code blocks.

### Setup Complete

- ✅ Comprehensive Markdown demonstration notebook created (`milestone_4_10_markdown.ipynb`)
- ✅ Examples of all major Markdown elements included
- ✅ Practice exercises and real-world examples prepared
- ✅ Quick guide documentation created

### Files Created for This Milestone

1. **`notebooks/milestone_4_10_markdown.ipynb`** - Complete Markdown formatting demonstration
2. **`MILESTONE_4_10_QUICK_GUIDE.md`** - Video recording guide with syntax reference

### Key Concepts

**Headings:**
- Structure notebooks with logical hierarchy
- Use `#` symbols (# for H1, ## for H2, etc.)
- Make navigation clear and intuitive

**Lists:**
- Unordered lists for bullet points (use `-`, `*`, or `+`)
- Ordered lists for sequential steps (use `1.`, `2.`, etc.)
- Nested lists for hierarchical information

**Inline Code:**
- Reference variables, functions, and short code snippets
- Use backticks: `` `code` ``
- Improves readability in explanatory text

**Code Blocks:**
- Display multi-line code without execution
- Use triple backticks with language: `` ```python ``
- Useful for showing examples and syntax

**Best Practice:**
- Markdown before code = explain intent
- Markdown after code = interpret results
- Avoid long explanations in code comments

### Quick Start

**Open the notebook in Jupyter:**

1. Make sure Jupyter is running (see Milestone 4.7)
2. Navigate to `notebooks/` folder
3. Open `milestone_4_10_markdown.ipynb`
4. Double-click Markdown cells to see raw syntax
5. Practice creating your own formatted cells

### Video Recording Requirements

Record a ~2 minute screen capture showing:
- ✅ Creating a new Markdown cell
- ✅ Writing headings at different levels
- ✅ Creating bulleted and numbered lists
- ✅ Using inline code (backticks)
- ✅ Creating code blocks (triple backticks)
- ✅ Explaining why Markdown documentation matters

### Key Syntax to Demonstrate

**Headings:** `#`, `##`, `###`

**Lists:**
- Bullets: `- item`
- Numbers: `1. item`

**Code:**
- Inline: `` `variable` ``
- Block: `` ```python ``

### Submission Checklist

- [ ] Opened `milestone_4_10_markdown.ipynb` in Jupyter
- [ ] Read through all Markdown examples
- [ ] Double-clicked cells to see raw syntax
- [ ] Created practice Markdown cells
- [ ] Recorded 2-minute walkthrough video showing:
  - Creating Markdown cells
  - Writing headings
  - Creating lists
  - Using inline code and code blocks
  - Explaining importance of documentation
- [ ] Video uploaded and link ready
- [ ] Pull Request created (if required)

### Documentation

For complete instructions and syntax reference, see **[MILESTONE_4_10_QUICK_GUIDE.md](MILESTONE_4_10_QUICK_GUIDE.md)**

### Status

**Current Status:** ✅ Setup Complete - Ready for Video Recording

**Next Action:** Open the notebook in Jupyter, study the examples, practice creating formatted Markdown, then record your demonstration following the quick guide.

---

## Milestone 4.11: Creating a Project Folder Structure for Data Science Work

### Objective

Create a clean, logical folder structure for Data Science projects that ensures clarity, reproducibility, and professionalism.

### Setup Complete

- ✅ Standard Data Science folder structure created
- ✅ Comprehensive README files for each folder
- ✅ Complete project structure documentation
- ✅ Quick guide for video recording

### Project Structure Created

```
S86-2426-Klyzer-Datascience-ShopWave/
│
├── data/                   # All datasets
│   ├── raw/               # Original, immutable data
│   └── processed/         # Cleaned, transformed data
│
├── notebooks/             # Jupyter notebooks for analysis
│
├── src/                   # Reusable Python scripts
│
├── outputs/               # Generated results
│   ├── figures/          # Plots and visualizations
│   └── reports/          # Generated reports
│
├── docs/                  # Project documentation
│
└── PROJECT_STRUCTURE.md  # Complete structure guide
```

### Files Created for This Milestone

1. **Folder Structure:**
   - `data/`, `data/raw/`, `data/processed/`
   - `notebooks/` (already existed)
   - `src/`
   - `outputs/`, `outputs/figures/`, `outputs/reports/`
   - `docs/`

2. **Documentation Files:**
   - `PROJECT_STRUCTURE.md` - Complete structure explanation
   - `data/README.md` - Data folder guidelines
   - `data/raw/README.md` - Raw data rules
   - `data/processed/README.md` - Processed data guidelines
   - `src/README.md` - Source code organization
   - `outputs/README.md` - Outputs organization
   - `docs/README.md` - Documentation guidelines
   - `MILESTONE_4_11_QUICK_GUIDE.md` - Video recording guide

### Key Concepts

**data/raw/**
- Original, unmodified source data
- NEVER edit files in this folder
- Read-only reference data

**data/processed/**
- Cleaned and transformed datasets
- Generated by scripts, not manually edited
- Ready for analysis and modeling

**notebooks/**
- Jupyter notebooks for exploration and analysis
- Document analysis with Markdown
- Keep notebooks focused and organized

**src/**
- Reusable Python scripts and functions
- Separate from notebooks for code reusability
- Modular, testable code

**outputs/**
- `figures/` - Plots and visualizations
- `reports/` - Generated reports and summaries
- Regenerable from source code

**docs/**
- Project documentation
- Data dictionaries
- Methodology notes
- Meeting notes and decisions

### Why This Structure Matters

✅ **Prevents confusion** - Clear separation of concerns

✅ **Protects data integrity** - Raw data stays untouched

✅ **Supports reproducibility** - Clear transformation trail

✅ **Enables collaboration** - Intuitive for teammates

✅ **Scales with growth** - Handles increasing complexity

### Video Recording Requirements

Record a ~2 minute screen capture showing:
- ✅ Root project folder overview
- ✅ Each subfolder and its purpose
- ✅ Why `data/raw/` vs `data/processed/` separation matters
- ✅ How `src/`, `notebooks/`, and `outputs/` work together
- ✅ Why good structure supports collaboration and reproducibility

### Key Points to Demonstrate

**Show the structure:**
- Navigate through each main folder
- Explain the purpose of each
- Show subfolders (raw/processed, figures/reports)

**Explain the principles:**
- Separation of raw and processed data
- Code (notebooks/src) vs results (outputs)
- Documentation (docs) for context
- How paths work between folders

**Why it matters:**
- Prevents lost files and confusion
- Supports reproducibility
- Makes collaboration easy
- Scales as projects grow

### Submission Checklist

- [ ] Created complete folder structure
- [ ] Reviewed README files in each folder
- [ ] Read `PROJECT_STRUCTURE.md`
- [ ] Recorded 2-minute walkthrough video showing:
  - Root folder and main folders
  - Purpose of each folder
  - data/raw/ vs data/processed/ distinction
  - How outputs/ organizes results
  - Why this structure supports good DS practice
- [ ] Video uploaded and link ready
- [ ] Pull Request created (if required)

### Documentation

For complete structure explanation, see **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)**

For video recording guide, see **[MILESTONE_4_11_QUICK_GUIDE.md](MILESTONE_4_11_QUICK_GUIDE.md)**

### Status

**Current Status:** ✅ Setup Complete - Ready for Video Recording

**Next Action:** Explore the folder structure, read the documentation in each folder, then record your demonstration following the quick guide. Use File Explorer or terminal (`tree` command) to show the structure clearly.

---

## Milestone 4.12: Organizing Raw Data, Processed Data, and Output Artifacts

### Overview

This milestone focuses on understanding the **data lifecycle**—from raw inputs to processed datasets and final outputs. Proper data organization prevents corruption, enables reproducibility, and maintains data integrity.

**Key Concept:** Data flows in ONE direction: **raw → processed → outputs**

### Learning Objectives

By completing this milestone, you will:

- ✅ Understand the difference between raw, processed, and output data
- ✅ Learn why raw data should **never** be modified
- ✅ Organize data into clearly defined folders
- ✅ Prevent accidental overwrites and data leakage
- ✅ Build habits that support reproducibility

### Three Data Stages

#### 1. Raw Data (`data/raw/`)

**Purpose:** Original, untouched source data

**Rules:**
- ✅ Store data exactly as received
- ✅ Treat as **READ-ONLY** (never modify)
- ✅ Keep original file names when possible
- ✅ Back up securely
- ❌ Never clean or edit raw files directly
- ❌ Never overwrite with processed versions

**Example:**
```
data/raw/
  └── sample_sales.csv    ← Original data, NEVER modified
```

#### 2. Processed Data (`data/processed/`)

**Purpose:** Cleaned, transformed, or filtered versions of raw data

**Rules:**
- ✅ Save cleaned/transformed datasets here
- ✅ Use descriptive names indicating processing stage
- ✅ Ensure these can be recreated from raw data + scripts
- ❌ Never mix with raw data
- ❌ Never save outputs here

**Example:**
```
data/processed/
  └── sample_sales_cleaned.csv    ← Derived from raw, reproducible
```

#### 3. Output Artifacts (`outputs/`)

**Purpose:** Final or intermediate results (visualizations, reports, models)

**Rules:**
- ✅ Store plots in `outputs/figures/`
- ✅ Store reports in `outputs/reports/`
- ✅ Use descriptive filenames
- ❌ Never save in data folders
- ❌ Never mix with input data

**Example:**
```
outputs/
  ├── figures/
  │   └── top_customers.png              ← Visualization
  └── reports/
      └── sales_summary_statistics.csv   ← Report
```

### Data Flow Diagram

```
data/raw/sample_sales.csv (ORIGINAL, READ-ONLY)
         ↓
    [LOAD & CLEAN]
         ↓
data/processed/sample_sales_cleaned.csv (REPRODUCIBLE)
         ↓
    [ANALYZE & VISUALIZE]
         ↓
    ┌──────────────┬──────────────┐
    ↓              ↓              ↓
outputs/       outputs/      outputs/
figures/       reports/      models/
```

### Why This Matters

**Common problems prevented:**
- 🔥 Raw data being overwritten accidentally
- 🔥 No record of how processed data was created
- 🔥 Outputs mixed with input data
- 🔥 Confusion about which files are final
- 🔥 Inability to reproduce results later

**Benefits of proper organization:**
- ✅ Raw data remains intact (data integrity)
- ✅ Processing steps are traceable (transparency)
- ✅ Outputs are clearly identifiable (clarity)
- ✅ Results can be reproduced reliably (reproducibility)

### Demonstrations

#### Working Example Notebook

**[data_lifecycle_demo.ipynb](notebooks/data_lifecycle_demo.ipynb)** - Complete demonstration:
- Loads raw data (read-only)
- Processes and saves to processed folder
- Analyzes processed data
- Generates outputs to correct locations
- Verifies all stages properly separated

#### Live Working Pipeline

**[structure_demo.ipynb](notebooks/structure_demo.ipynb)** - Real data pipeline:
1. Imports custom functions from `src/data_processing.py`
2. Loads raw data from `data/raw/sample_sales.csv` (never modifies it!)
3. Cleans and saves to `data/processed/`
4. Performs analysis ($929.82 revenue calculated)
5. Generates visualization → `outputs/figures/`
6. Creates report → `outputs/reports/`

### Key Principles

#### ⚠️ What NOT to Do

```python
# ❌ BAD - Overwrites raw data!
df = pd.read_csv('data/raw/sales.csv')
df = df.dropna()
df.to_csv('data/raw/sales.csv')  # DANGER! Original lost forever!
```

#### ✅ What TO Do

```python
# ✅ GOOD - Preserves raw data
df = pd.read_csv('data/raw/sales.csv')         # Load raw (read-only)
df_cleaned = df.dropna()                       # Process in memory
df_cleaned.to_csv('data/processed/sales_cleaned.csv')  # Save separately
```

### Video Walkthrough Requirements (~2 Minutes)

Your video must include:

1. **Raw data folder** - Show location, explain read-only principle
2. **Processed data folder** - Show derived datasets, explain reproducibility
3. **Output artifacts folder** - Show figures and reports organization
4. **Data flow demonstration** - Run notebook showing raw → processed → outputs
5. **Rationale** - Explain why separation prevents corruption and enables reproducibility

### Documentation

For detailed principles and examples:
- **[DATA_ORGANIZATION_GUIDE.md](DATA_ORGANIZATION_GUIDE.md)** - Complete data lifecycle guide
- **[MILESTONE_4_12_QUICK_GUIDE.md](MILESTONE_4_12_QUICK_GUIDE.md)** - Video script and checklist
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Overall project organization

### Submission Checklist

- [ ] Reviewed data lifecycle principles
- [ ] Examined `data/raw/`, `data/processed/`, `outputs/` folders
- [ ] Read `DATA_ORGANIZATION_GUIDE.md`
- [ ] Ran `data_lifecycle_demo.ipynb` notebook
- [ ] Recorded 2-minute walkthrough video showing:
  - Raw data folder and read-only rule
  - Processed data folder and reproducibility
  - Output folders organization
  - Live demonstration of data flow
  - Explanation of why separation matters
- [ ] Video uploaded and link ready
- [ ] Pull Request created (if required)

### Status

**Current Status:** ✅ Setup Complete - Ready for Testing and Video Recording

**Files Created:**
- ✅ `data/raw/sample_sales.csv` - Sample raw data
- ✅ `data/processed/sample_sales_cleaned.csv` - Sample processed data
- ✅ `outputs/figures/top_customers.png` - Sample visualization
- ✅ `outputs/reports/sales_summary_statistics.csv` - Sample report
- ✅ `notebooks/data_lifecycle_demo.ipynb` - Complete walkthrough notebook
- ✅ `DATA_ORGANIZATION_GUIDE.md` - Comprehensive documentation

**Next Action:** Run `data_lifecycle_demo.ipynb` to see the complete data lifecycle in action, then record your demonstration following the quick guide.

---

## Milestone 4.16: Writing Conditional Statements for Data Logic

### Objective

Use Python conditional statements to control program flow using clear, correct decision logic.

### Files Created for This Milestone

1. **`src/conditional_statements_demo.py`** - Standalone conditional logic script
2. **`MILESTONE_4_16_QUICK_GUIDE.md`** - Quick guide, checklist, and 2-minute video script

### Quick Start

Run from project root:

```powershell
python src/conditional_statements_demo.py
```

### What This Demonstrates

- Basic `if` statement
- `if-else` branching
- `if-elif-else` with multiple outcomes
- Numeric and string comparisons
- Logical operators: `and`, `or`, `not`
- Edge-case threshold handling

### Video Recording Requirements (~2 Minutes)

Record a short screen capture showing:
- ✅ A simple `if` example
- ✅ An `if-else` example
- ✅ An `if-elif-else` example
- ✅ Logical operators in action
- ✅ Explanation of decision outcomes

### Documentation

For complete walkthrough steps, use **[MILESTONE_4_16_QUICK_GUIDE.md](MILESTONE_4_16_QUICK_GUIDE.md)**

---

## Milestone 4.17: Using for and while Loops for Iterative Data Processing

### Objective

Use Python loops to process repeated logic safely and clearly.

### Files Created for This Milestone

1. **`src/loops_iterative_processing_demo.py`** - Standalone loops demo script
2. **`MILESTONE_4_17_QUICK_GUIDE.md`** - Quick guide, checklist, and 2-minute video script

### Quick Start

Run from project root:

```powershell
python src/loops_iterative_processing_demo.py
```

### What This Demonstrates

- `for` loop with range iteration
- `for` loop with list iteration
- `while` loop with condition-based repetition
- Loop control using `break` and `continue`
- Safe loop termination patterns to avoid infinite loops

### Video Recording Requirements (~2 Minutes)

Record a short screen capture showing:
- ✅ A `for` loop example
- ✅ A `while` loop example
- ✅ Use of `break` or `continue`
- ✅ Explanation of loop behavior and flow

### Documentation

For complete walkthrough steps, use **[MILESTONE_4_17_QUICK_GUIDE.md](MILESTONE_4_17_QUICK_GUIDE.md)**

---

## Milestone 4.18: Defining and Calling Python Functions

### Objective

Use Python functions to organize code into reusable, logical blocks.

### Files Created for This Milestone

1. **`src/functions_definition_calling_demo.py`** - Standalone functions demo script
2. **`MILESTONE_4_18_QUICK_GUIDE.md`** - Quick guide, checklist, and 2-minute video script

### Quick Start

Run from project root:

```powershell
python src/functions_definition_calling_demo.py
```

### What This Demonstrates

- Defining functions with `def`
- Calling functions from `main()`
- Using parameters and arguments
- Returning values and reusing results
- Basic local vs global scope behavior

### Video Recording Requirements (~2 Minutes)

Record a short screen capture showing:
- ✅ Defining at least one function
- ✅ Calling the function
- ✅ Passing arguments
- ✅ Explaining execution flow

### Documentation

For complete walkthrough steps, use **[MILESTONE_4_18_QUICK_GUIDE.md](MILESTONE_4_18_QUICK_GUIDE.md)**

---

## Milestone 4.19: Passing Data into Functions and Returning Results

### Objective

Use Python functions as reusable input-output units by passing arguments and returning computed results.

### Files Created for This Milestone

1. **`src/functions_input_output_demo.py`** - Standalone functions input/output demo
2. **`MILESTONE_4_19_QUICK_GUIDE.md`** - Quick guide, checklist, and 2-minute video script

### Quick Start

Run from project root:

```powershell
python src/functions_input_output_demo.py
```

### What This Demonstrates

- Defining functions with parameters
- Passing arguments during function calls
- Returning values with `return`
- Storing and reusing returned results
- Clear and predictable input-output behavior

### Video Recording Requirements (~2 Minutes)

Record a short screen capture showing:
- ✅ A function with parameters
- ✅ Passing arguments into the function
- ✅ Returning a value
- ✅ Using the returned result elsewhere

### Documentation

For complete walkthrough steps, use **[MILESTONE_4_19_QUICK_GUIDE.md](MILESTONE_4_19_QUICK_GUIDE.md)**

---

## Milestone 4.20: Writing Readable Variable Names and Comments (PEP 8 Basics)

### Objective

Improve Python code readability using descriptive naming and meaningful comments.

### Files Created for This Milestone

1. **`src/readable_naming_comments_demo.py`** - Standalone readability demo script
2. **`MILESTONE_4_20_QUICK_GUIDE.md`** - Quick guide, checklist, and 2-minute video script

### Quick Start

Run from project root:

```powershell
python src/readable_naming_comments_demo.py
```

### What This Demonstrates

- Good vs poor variable naming examples
- PEP 8 snake_case naming for variables
- Uppercase constant naming
- Useful comments that explain intent
- Common readability mistakes to avoid

### Video Recording Requirements (~2 Minutes)

Record a short screen capture showing:
- ✅ Good vs poor variable names
- ✅ Corrected variable names using PEP 8
- ✅ Useful comments in context
- ✅ Explanation of why readability matters

### Documentation

For complete walkthrough steps, use **[MILESTONE_4_20_QUICK_GUIDE.md](MILESTONE_4_20_QUICK_GUIDE.md)**