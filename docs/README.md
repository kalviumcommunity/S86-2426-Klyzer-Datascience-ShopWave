# Documentation (docs)

**Purpose:** Project documentation, guides, and references

## Purpose

This folder contains:
- Project documentation
- Data dictionaries
- Methodology notes
- Meeting notes
- Technical specifications
- User guides

## What Goes Here

✅ Store:
- Project overview documents
- Data dictionaries (column descriptions)
- Methodology documentation
- Meeting notes and decisions
- Technical specifications
- User guides or instructions
- Literature references

❌ Do NOT store:
- Source code (use `src/`)
- Notebooks (use `notebooks/`)
- Generated reports (use `outputs/reports/`)
- Data files (use `data/`)

## Common Documents

```
docs/
├── project_overview.md       # Project goals and scope
├── data_dictionary.md        # Column names and descriptions
├── methodology.md            # Analysis approach
├── meeting_notes.md          # Team decisions
├── references.md             # Literature and resources
└── changelog.md              # Project history
```

## Example: data_dictionary.md

```markdown
# Data Dictionary

## sales_2024.csv

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| customer_id | int | Unique customer identifier | 12345 |
| order_date | date | Date of purchase | 2024-01-15 |
| product_id | int | Product identifier | 98765 |
| quantity | int | Number of items purchased | 3 |
| price | float | Unit price in USD | 29.99 |
| total_amount | float | Total transaction value | 89.97 |

## customers.json

| Field | Type | Description |
|-------|------|-------------|
| id | integer | Customer ID |
| name | string | Customer full name |
| email | string | Contact email |
| signup_date | string | Registration date (ISO format) |
```

## Example: methodology.md

```markdown
# Analysis Methodology

## Data Collection
- Source: Company sales database
- Period: January 2024 - December 2024
- Extraction date: 2024-12-31

## Data Processing
1. Remove duplicate transactions
2. Handle missing values in quantity field (fill with 0)
3. Filter out test accounts (customer_id < 1000)
4. Calculate derived metrics

## Analysis Approach
1. Exploratory Data Analysis (EDA)
2. Descriptive statistics
3. Trend analysis
4. Customer segmentation
5. Predictive modeling

## Tools Used
- Python 3.12
- pandas, numpy for data processing
- matplotlib, seaborn for visualization
- scikit-learn for modeling
```

## Best Practices

✅ **DO:**
- Keep documentation updated
- Use clear, concise language
- Include examples and context
- Version control documentation
- Make it easy for others to understand

❌ **DON'T:**
- Let documentation become outdated
- Use jargon without explanation
- Skip documenting important decisions
- Assume everyone has context

## When to Update docs/

Update documentation when:
- Starting a new project (create project overview)
- Receiving new data (update data dictionary)
- Making methodology changes (document decisions)
- After team meetings (capture decisions)
- Finding useful references (add to references.md)
