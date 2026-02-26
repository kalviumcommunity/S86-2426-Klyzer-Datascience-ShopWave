# Raw Data

**Purpose:** Original, immutable source data

## Important Rules

⚠️ **NEVER modify files in this folder**

- This folder contains the original, unprocessed data
- Treat these files as read-only
- Any transformations should create new files in `data/processed/`

## What Goes Here

✅ Store:
- Downloaded datasets (CSV, Excel, JSON, etc.)
- API responses saved to files
- Database dumps
- Any original source data

❌ Do NOT store:
- Cleaned or transformed data (use `data/processed/`)
- Analysis results (use `outputs/`)
- Temporary files

## Usage

```python
# Good: Read from raw data
import pandas as pd
df = pd.read_csv('../data/raw/sales_2024.csv')

# Process the data
df_cleaned = clean_data(df)

# Save to processed folder
df_cleaned.to_csv('../data/processed/sales_cleaned.csv', index=False)
```

## Git Considerations

Large data files should typically be excluded from version control:
- Add `*.csv`, `*.xlsx`, etc. to `.gitignore`
- Document data sources in the main README
- Consider using data version control tools (DVC) for larger projects
