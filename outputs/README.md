# Outputs

**Purpose:** Generated results, visualizations, and reports

## Structure

```
outputs/
├── figures/   # Plots, charts, and visualizations
└── reports/   # Generated reports and summaries
```

## Guidelines

### `figures/` folder
- **Purpose:** Store all plots and visualizations
- **Formats:** PNG, JPG, SVG, PDF
- **Usage:** Charts, graphs, diagrams generated from analysis
- **Examples:** Distribution plots, correlation heatmaps, model performance charts

### `reports/` folder
- **Purpose:** Store generated reports and summaries
- **Formats:** PDF, HTML, Markdown, Excel
- **Usage:** Final reports, executive summaries, data reports
- **Examples:** Analysis reports, model evaluation summaries, slide decks

## What Goes Here

✅ Store:
- Plots and visualizations
- Generated reports
- Model evaluation results
- Summary statistics files
- Exported presentations

❌ Do NOT store:
- Raw or processed data (use `data/`)
- Source code (use `src/` or `notebooks/`)
- Notebooks (use `notebooks/`)

## Naming Conventions

Use descriptive names with dates if needed:

```
figures/
├── sales_distribution.png
├── correlation_heatmap.png
├── model_performance_2024_01.png
└── feature_importance.svg

reports/
├── monthly_analysis_2024_01.pdf
├── model_evaluation_report.html
└── executive_summary.md
```

## Usage Examples

### Saving Figures

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Create visualization
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='sales')
plt.title('Sales Distribution')

# Save to outputs/figures/
plt.savefig('../outputs/figures/sales_distribution.png', 
            dpi=300, bbox_inches='tight')
plt.close()
```

### Generating Reports

```python
import pandas as pd

# Generate summary statistics
summary = df.describe()

# Save to outputs/reports/
summary.to_csv('../outputs/reports/data_summary.csv')
summary.to_html('../outputs/reports/data_summary.html')
```

## Best Practices

✅ **DO:**
- Use high resolution for figures (dpi=300)
- Include descriptive filenames
- Version outputs if needed (with dates)
- Keep outputs organized by type
- Document how outputs were generated

❌ **DON'T:**
- Store temporary or draft figures
- Mix different output types
- Use generic names like "plot1.png"
- Commit large output files to git

## Git Considerations

Outputs are typically excluded from version control:
- Add `outputs/` to `.gitignore`
- Outputs can be regenerated from code
- Share final reports separately if needed
- Keep notebooks and scripts version-controlled instead
