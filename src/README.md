# Source Code (src)

**Purpose:** Reusable Python scripts and modules

## Purpose

This folder contains:
- Python scripts with reusable functions
- Data processing pipelines
- Model training scripts
- Utility functions
- Custom modules

## What Goes Here

✅ Store:
- `.py` files with reusable code
- Data cleaning functions
- Feature engineering scripts
- Model training pipelines
- Helper utilities
- Custom classes and functions

❌ Do NOT store:
- Jupyter notebooks (use `notebooks/`)
- Data files (use `data/`)
- Results or outputs (use `outputs/`)
- Documentation (use `docs/`)

## Structure Example

```
src/
├── data_processing.py      # Data cleaning and transformation
├── feature_engineering.py  # Feature creation functions
├── model_training.py       # Model training pipelines
├── visualization.py        # Plotting utilities
├── utils.py               # General helper functions
└── config.py              # Configuration settings
```

## Why Separate Scripts from Notebooks?

**Notebooks are for:**
- Exploration and experimentation
- Visualization and analysis
- Documentation and storytelling

**Scripts (src/) are for:**
- Reusable, production-ready code
- Functions used across multiple notebooks
- Automated pipelines
- Version-controlled logic

## Usage in Notebooks

```python
# In a Jupyter notebook
import sys
sys.path.append('../src')

# Import your custom functions
from data_processing import clean_data, handle_missing_values
from feature_engineering import create_features
from visualization import plot_distribution

# Use them
df_cleaned = clean_data(df)
df_featured = create_features(df_cleaned)
plot_distribution(df_featured, 'sales')
```

## Best Practices

✅ **DO:**
- Write modular, reusable functions
- Add docstrings to functions
- Follow PEP 8 style guidelines
- Test your functions
- Keep functions focused and single-purpose

❌ **DON'T:**
- Copy-paste code between notebooks
- Mix exploratory code with production code
- Leave functions undocumented
- Create overly complex modules

## Example: data_processing.py

```python
"""
Data processing utilities for sales analysis project.
"""

import pandas as pd
import numpy as np

def clean_data(df):
    """
    Clean the input dataframe by handling missing values and duplicates.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Raw data to be cleaned
        
    Returns:
    --------
    pandas.DataFrame
        Cleaned dataframe
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna(subset=['customer_id'])
    df['sales'] = df['sales'].fillna(0)
    
    return df

def validate_data(df):
    """
    Validate data quality and print summary.
    """
    print(f"Shape: {df.shape}")
    print(f"Missing values:\\n{df.isnull().sum()}")
    print(f"Duplicates: {df.duplicated().sum()}")
```

## When to Create a Script

Create a `.py` script when:
- You're using the same function in multiple notebooks
- Your notebook is getting too long or complex
- You want to version control logic separately
- You're building a data pipeline
- You need to automate processes
