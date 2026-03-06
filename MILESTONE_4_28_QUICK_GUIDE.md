# Milestone 4.28 - Creating Pandas DataFrames Quick Guide

## Video Recording Requirements
- **Duration**: ~2 minutes
- **Format**: Screen-facing, clearly visible
- **Content**: Must demonstrate creating DataFrames from dictionaries and files

---

## 2-Minute Video Script

### Opening (10 seconds)
"Hi! Today I'm demonstrating Pandas DataFrames - the primary structure for tabular data in Pandas. A DataFrame is like a spreadsheet or database table with rows and columns."

**Show on screen**: Open `milestone_4_28_pandas_dataframes.ipynb`

---

### Section 1: Creating DataFrame from Dictionary (40 seconds)
**0:10 - 0:50**

"Let's create a DataFrame from a Python dictionary."

```python
import pandas as pd

# Dictionary with column data
student_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Score': [85, 92, 78]
}

# Create DataFrame
df = pd.DataFrame(student_data)
print(df)
```

**Explain**: "In the dictionary, keys become column names and values become column data. Look at the output - we have row indexes on the left (0, 1, 2), column names on top, and our data in the middle."

**Show the output**:
```
      Name  Age  Score
0    Alice   25     85
1      Bob   30     92
2  Charlie   22     78
```

**Key points**: 
- "Keys = column names"
- "Values = column data" 
- "Automatic index creation"

```python
print("\nShape:", df.shape)
print("Columns:", list(df.columns))
```

**Explain**: "Shape tells us (rows, columns). We have 3 rows and 3 columns. Always check your shape after creating a DataFrame!"

---

### Section 2: Loading DataFrame from CSV (40 seconds)
**0:50 - 1:30**

"Now let's load data from a CSV file - this is how you'll work with real data."

```python
# Load CSV file
df_from_csv = pd.read_csv('../data/raw/sample_data.csv')

print("Loaded from CSV:")
print(df_from_csv)
```

**Show the CSV file content first** (optional):
```
Name,Age,City,Score
Alice,25,New York,85
Bob,30,Los Angeles,92
Charlie,22,Chicago,78
```

**Explain**: "pd.read_csv() automatically reads the first row as column names and creates a DataFrame. The file path points to where your CSV is stored."

**Show the output**:
```
      Name  Age         City  Score
0    Alice   25     New York     85
1      Bob   30  Los Angeles     92
2  Charlie   22      Chicago     78
3    Diana   28      Houston     95
4     Emma   26      Phoenix     88
```

**Demonstrate basic inspection**:
```python
print("\nFirst 3 rows:")
print(df_from_csv.head(3))

print("\nDataFrame info:")
print(df_from_csv.info())
```

**Explain**: "Always use .head() to preview your data and .info() to check data types and missing values."

---

### Section 3: Inspecting DataFrames (25 seconds)
**1:30 - 1:55**

"After loading data, always inspect it!"

```python
# Essential inspection methods
print("Shape:", df_from_csv.shape)
print("Columns:", list(df_from_csv.columns))
print("\nFirst few rows:")
print(df_from_csv.head())
```

**Explain**: "Shape shows (rows, columns). Columns lists all column names. head() shows the first 5 rows by default."

**Show one more useful method**:
```python
print("\nSummary statistics:")
print(df_from_csv.describe())
```

**Explain**: "describe() gives you statistical summary for numeric columns - count, mean, std, min, max, and quartiles."

---

### Section 4: Why DataFrames Matter (5 seconds)
**1:55 - 2:00**

"DataFrames are the working table for all data analysis in Pandas. They make tabular data easy to manipulate, clean, and analyze."

**Closing**: "Master DataFrames and you master Pandas! Thanks for watching!"

---

## Success Criteria (Must Show All)

### ✅ Required Demonstrations:
1. **Import Pandas** - `import pandas as pd`
2. **Create DataFrame from dictionary** - show code and output
3. **Load DataFrame from CSV** - `pd.read_csv()` with output
4. **Inspect structure** - use `.head()`, `.shape`, or `.info()`
5. **Show rows and columns** - display actual data
6. **Explain tabular structure** - mention rows, columns, index

### ✅ Must Be Visible:
- DataFrame output showing index, columns, and data
- File path for CSV loading
- At least one inspection method (.head(), .info(), or .describe())
- Column names clearly visible
- Explanation of DataFrame purpose

---

## Code Examples for Video

### Example 1: Dictionary to DataFrame (Use This!)
```python
import pandas as pd

# Create from dictionary
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [999, 25, 75],
    'Stock': [15, 120, 85]
}

df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)
```

**Expected output**:
```
    Product  Price  Stock
0    Laptop    999     15
1     Mouse     25    120
2  Keyboard     75     85

Shape: (3, 3)
```

---

### Example 2: Load from CSV (Use This!)
```python
# Load CSV
df_csv = pd.read_csv('../data/raw/sample_data.csv')

print("Loaded DataFrame:")
print(df_csv)

print("\nInfo:")
df_csv.info()
```

**Expected output**:
```
Loaded DataFrame:
      Name  Age         City  Score
0    Alice   25     New York     85
1      Bob   30  Los Angeles     92
2  Charlie   22      Chicago     78
3    Diana   28      Houston     95
4     Emma   26      Phoenix     88

Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    5 non-null      object
 1   Age     5 non-null      int64 
 2   City    5 non-null      object
 3   Score   5 non-null      int64 
dtypes: int64(2), object(2)
memory usage: 288.0+ bytes
```

---

### Example 3: Inspection Methods (Use This!)
```python
# Inspection
print("First 3 rows:")
print(df_csv.head(3))

print("\nShape:", df_csv.shape)
print("Columns:", list(df_csv.columns))

print("\nStatistics:")
print(df_csv.describe())
```

---

## Common Mistakes to Avoid in Video

### ❌ Don't Do:
1. **Forget to import Pandas** - Always `import pandas as pd`
2. **Skip inspection** - Always show .head() or .info()
3. **Wrong file path** - Make sure CSV exists and path is correct
4. **Assume structure** - Show the actual DataFrame output
5. **Rush through inspection** - Take time to explain what you're seeing

### ✓ Do:
1. **Show the dictionary structure** - Explain keys = columns
2. **Print the DataFrame** - Display the tabular output
3. **Show .shape and .columns** - Verify the structure
4. **Use real CSV file** - Demonstrate actual file loading
5. **Inspect after loading** - Demonstrate .head() or .info()

---

## Timing Breakdown

| Time | Section | Content |
|------|---------|---------|
| 0:00-0:10 | Intro | What is a DataFrame |
| 0:10-0:50 | From Dict | Create DataFrame from dictionary |
| 0:50-1:30 | From CSV | Load from file with pd.read_csv() |
| 1:30-1:55 | Inspection | .head(), .shape, .describe() |
| 1:55-2:00 | Why | Importance of DataFrames, closing |

---

## Troubleshooting

### If CSV File Not Found:
- Check the file path is correct
- Use absolute path if needed: `C:/path/to/file.csv`
- Create the CSV first (show in video if needed)

### If You Run Out of Time:
- Combine inspection methods (show .head() only)
- Skip .describe() demonstration
- Focus on creation and basic structure

### If You Have Extra Time:
- Show selecting a column: `df['Name']`
- Demonstrate filtering: `df[df['Age'] > 25]`
- Show adding a new column

### Voice-over Tips:
- Emphasize "rows and columns"
- Use phrase "tabular data" or "spreadsheet-like"
- Pause after outputs appear
- Explain each component: index, columns, values

---

## Key Phrases to Use

1. "DataFrame is the primary structure for tabular data"
2. "Dictionary keys become column names"
3. "pd.read_csv() loads data from files"
4. "Always inspect your data after loading"
5. "Rows have indexes, columns have names"
6. "DataFrames are like spreadsheets in Pandas"
7. "Check shape, columns, and first few rows"
8. "DataFrames are built from Series"

---

## After Recording Checklist

- [ ] Video shows Pandas import
- [ ] Created DataFrame from dictionary
- [ ] Loaded DataFrame from CSV file
- [ ] Showed DataFrame output with index/columns/data
- [ ] Demonstrated at least one inspection method
- [ ] Explained DataFrame structure (rows, columns)
- [ ] Mentioned why DataFrames are useful
- [ ] Video is approximately 2 minutes
- [ ] Code outputs are clearly visible
- [ ] Explanations are clear and audible
- [ ] No background noise or distractions
- [ ] Screen is clearly visible throughout

---

## Quick Reference: DataFrame Creation

```python
# Method 1: From dictionary (column-oriented)
df = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': [4, 5, 6]
})

# Method 2: From dictionary (row-oriented)
df = pd.DataFrame([
    {'col1': 1, 'col2': 4},
    {'col1': 2, 'col2': 5}
])

# Method 3: From CSV file
df = pd.read_csv('file.csv')

# Method 4: From NumPy array
df = pd.DataFrame(np_array, columns=['A', 'B', 'C'])
```

---

## Essential Inspection Methods

```python
# Preview data
df.head()        # First 5 rows
df.tail()        # Last 5 rows
df.head(3)       # First 3 rows

# Structure
df.shape         # (rows, columns)
df.columns       # Column names
df.index         # Row index
df.dtypes        # Data types

# Information  
df.info()        # Comprehensive overview
df.describe()    # Statistical summary

# Missing data
df.isnull()      # Check for nulls
df.isnull().sum()  # Count nulls per column
```

---

## DataFrame Anatomy

```
DataFrame Structure:
                     ← Columns →
        Name    Age    Score
    ↑   Alice    25      85      ← Row 0
    |   Bob      30      92      ← Row 1
Index   Charlie  22      78      ← Row 2
    ↓

Components:
- Index: Row labels (0, 1, 2...)
- Columns: Column names (Name, Age, Score)
- Values: Actual data (Alice, 25, 85...)
```

---

## Comparison: Series vs DataFrame

| Feature | Series | DataFrame |
|---------|--------|-----------|
| Dimensions | 1D | 2D |
| Structure | Single column | Multiple columns |
| Use Case | One variable | Multiple variables |
| Example | Temperatures | Student records |
| Access | `series[0]` | `df['column']` or `df.iloc[0]` |

---

## Final Notes

- **Keep it simple**: Focus on creation and basic inspection
- **Show outputs**: The tabular display is key
- **Explain structure**: Index, columns, values
- **Demonstrate loading**: CSV is most common
- **Always inspect**: .head(), .info(), .shape

**Remember**: DataFrame = 2D table. That's the core concept!

Good luck with your recording! 🎥
