# Milestone 4.41: Identifying Trends Over Time Using Line Plots - 2-Minute Video Guide

**Total Time: 2 minutes (120 seconds)**

---

## SUCCESS CRITERIA

Your video must demonstrate **ALL 5 of these operations**:

1. [x] **Load Time-Based Data** and identify the date column
2. [x] **Convert and Sort by Time** before plotting
3. [x] **Create a Line Plot** with time on x-axis and numeric value on y-axis
4. [x] **Interpret Trend Direction** (upward, downward, stable)
5. [x] **Point Out Notable Changes** (spikes, drops, volatility)

**Note:** If any of these 5 are missing, record again.

---

## VIDEO STRUCTURE & TIMING

### Introduction (0:00-0:10) - 10 seconds

**What to say:**
> "Hi, I am [Your Name]. This is Milestone 4.41 on identifying trends over time using line plots. I will show how ordering by time and plotting a line helps reveal trends and changes clearly."

**What to show:**
- Notebook title
- Time-based dataset loaded

---

### Section 1: Load Data and Prepare Time Column (0:10-0:35) - 25 seconds

**What to say:**
> "First, I load the sales data, convert `OrderDate` to datetime, and sort by date. Time order is essential because line plots connect points sequentially."

**What to show:**
```python
import pandas as pd
import matplotlib.pyplot as plt

sales_df = pd.read_csv('../data/raw/sales_data.csv')
sales_df['OrderDate'] = pd.to_datetime(sales_df['OrderDate'])
sales_df = sales_df.sort_values('OrderDate')

print(sales_df[['OrderDate', 'Quantity', 'Price']].head())
```

**Key point:** "Always sort by time before plotting trends."

---

### Section 2: Create a Line Plot (0:35-1:00) - 25 seconds

**What to say:**
> "Now I create a line plot with `OrderDate` on the x-axis and `Price` on the y-axis. Line plots are ideal because they show continuity and change across time."

**What to show:**
```python
plt.figure(figsize=(9, 4))
plt.plot(sales_df['OrderDate'], sales_df['Price'], marker='o')
plt.title('Price Trend Over Time')
plt.xlabel('Order Date')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Interpretation to say:**
- "The connected points show how values evolve over time."
- "Direction of the line helps identify trend behavior."

---

### Section 3: Identify Trends and Pattern Type (1:00-1:25) - 25 seconds

**What to say:**
> "Now I summarize whether the pattern looks upward, downward, or mixed. I avoid judging trend from a single point and focus on overall direction."

**What to show:**
```python
print('Price summary over time:')
print(sales_df['Price'].describe())

start_price = sales_df['Price'].iloc[0]
end_price = sales_df['Price'].iloc[-1]
print('Start price:', start_price)
print('End price:', end_price)
```

**Interpretation tip:**
- Start vs end is useful but not enough by itself
- Consider full pattern, not only endpoints

---

### Section 4: Spot Changes and Anomalies (1:25-1:50) - 25 seconds

**What to say:**
> "I now highlight notable changes like spikes or sudden drops. These may reflect important events, noise, or irregular behavior and should trigger deeper questions."

**What to show:**
```python
sales_df['price_change'] = sales_df['Price'].diff()
print('Largest increases:')
print(sales_df.nlargest(2, 'price_change')[['OrderDate', 'Price', 'price_change']])

print('\nLargest drops:')
print(sales_df.nsmallest(2, 'price_change')[['OrderDate', 'Price', 'price_change']])
```

**Key point:** "Spikes and drops are signals for investigation, not instant conclusions."

---

### Wrap-Up (1:50-2:00) - 10 seconds

**What to say:**
> "Key takeaway: line plots help us read the story of data over time. Sorting by date and interpreting overall patterns leads to better EDA decisions."

**What to show:**
- Final line plot and one short trend insight

---

## TROUBLESHOOTING GUIDE

### Problem 1: "Line plot looks random"

**Cause:** Data is not sorted by date.

**Fix:**
```python
sales_df = sales_df.sort_values('OrderDate')
```

---

### Problem 2: "Date axis appears incorrect"

**Cause:** Date column is still string type.

**Fix:**
```python
sales_df['OrderDate'] = pd.to_datetime(sales_df['OrderDate'])
```

---

### Problem 3: "Too many lines cluttering the chart"

**Cause:** Plotting too many variables at once.

**Fix:**
- Start with one clear line
- Add one more line only if comparison is needed

Keep trend visuals simple and readable.

---

## FINAL CHECKLIST BEFORE SUBMITTING

- [ ] Loaded dataset with time column
- [ ] Converted and sorted data by date/time
- [ ] Created a line plot with proper axis labels
- [ ] Explained observed trend direction
- [ ] Pointed out spikes, drops, or volatile periods
- [ ] Explained why line plots fit temporal analysis
- [ ] Recorded a clear ~2-minute walkthrough video
- [ ] Included PR/video link as required

You are now ready to identify and explain trends over time using line plots.
