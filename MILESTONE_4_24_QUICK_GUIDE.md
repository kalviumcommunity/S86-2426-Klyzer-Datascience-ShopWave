# Milestone 4.24: Performing Basic Mathematical Operations on NumPy Arrays

## Quick Reference Guide for Video Recording

---

## Video Requirements

**Duration:** ~2 minutes  
**Format:** Screen capture showing Jupyter Notebook  
**Focus:** Basic mathematical operations on arrays

---

## Video Script (~2 Minutes)

### Introduction (10 seconds)

"Hi, this is [Your Name] demonstrating Milestone 4.24: Performing Basic Mathematical Operations on NumPy Arrays."

---

### 1. Element-Wise Array Operations (30 seconds)

**What to show:**
```python
import numpy as np

# Create two arrays
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

# Element-wise operations
print(f"Addition: {arr1 + arr2}")      # [11 22 33 44]
print(f"Subtraction: {arr1 - arr2}")   # [9 18 27 36]
print(f"Multiplication: {arr1 * arr2}") # [10 40 90 160]
print(f"Division: {arr1 / arr2}")      # [10. 10. 10. 10.]
```

**What to say:**
- "NumPy performs operations element-by-element"
- "arr1 + arr2 adds corresponding elements: 10+1=11, 20+2=22, etc."
- "This works for all arithmetic operations"
- "No loops needed - NumPy handles this automatically"

---

### 2. Scalar Operations (25 seconds)

**What to show:**
```python
arr = np.array([10, 20, 30, 40, 50])

print(f"Add 5: {arr + 5}")        # [15 25 35 45 55]
print(f"Multiply by 2: {arr * 2}") # [20 40 60 80 100]
print(f"Square: {arr ** 2}")      # [100 400 900 1600 2500]
```

**What to say:**
- "You can apply a single value to an entire array"
- "This is called scalar broadcasting"
- "The scalar is automatically applied to every element"
- "Extremely useful for data transformations"

---

### 3. NumPy Arrays vs Python Lists (25 seconds)

**What to show:**
```python
# Python list behavior
my_list = [1, 2, 3]
print(f"List + List: {my_list + my_list}")  # [1, 2, 3, 1, 2, 3] - concatenation
print(f"List * 2: {my_list * 2}")           # [1, 2, 3, 1, 2, 3] - repetition

# NumPy array behavior
my_array = np.array([1, 2, 3])
print(f"Array + Array: {my_array + my_array}")  # [2 4 6] - addition
print(f"Array * 2: {my_array * 2}")             # [2 4 6] - multiplication
```

**What to say:**
- "Lists and arrays behave very differently with operators"
- "List + list concatenates; array + array adds mathematically"
- "List * 2 repeats; array * 2 multiplies each element"
- "This is why NumPy is essential for numerical work"

---

### 4. Practical Example (20 seconds)

**What to show:**
```python
# Temperature conversion: Celsius to Fahrenheit
celsius = np.array([0, 10, 20, 30, 100])
fahrenheit = celsius * 9/5 + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
# [32. 50. 68. 86. 212.]
```

**What to say:**
- "Here's a real-world example: temperature conversion"
- "The formula C * 9/5 + 32 applies to the entire array"
- "No loop needed - one line converts all temperatures"
- "This is the power of NumPy for data operations"

---

### 5. Avoiding Common Mistakes (15 seconds)

**What to show:**
```python
# Shape mismatch
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30, 40])  # Different size

print(f"Shape 1: {arr1.shape}")  # (3,)
print(f"Shape 2: {arr2.shape}")  # (4,)
print("arr1 + arr2 would cause ValueError: incompatible shapes")
```

**What to say:**
- "Always check array shapes before operations"
- "Arrays must have compatible shapes for element-wise operations"
- "Shape mismatch causes errors"
- "Use .shape to verify before operating"

---

### Closing (5 seconds)

"That's Milestone 4.24 complete. I've demonstrated element-wise operations, scalar broadcasting, and how NumPy differs from Python lists. Thank you!"

---

## Key Points to Emphasize

### Must Cover:
1. ✅ **Element-wise operations** - Operations apply to corresponding elements
2. ✅ **Scalar broadcasting** - Single values apply to entire arrays
3. ✅ **Arrays vs lists** - Different behavior with + and * operators
4. ✅ **No loops needed** - NumPy handles iteration automatically
5. ✅ **Shape compatibility** - Arrays must have matching shapes

### Important Concepts:
- **Vectorization** - Operations on entire arrays without explicit loops
- **Broadcasting** - Automatic expansion of scalars to array shape
- **Mathematical operators** - +, -, *, /, ** all work element-wise
- **Efficiency** - NumPy is much faster than Python loops

---

## Common Mistakes to Avoid During Recording

❌ Using loops to perform array operations  
❌ Expecting list behavior from arrays  
❌ Operating on arrays with incompatible shapes without explanation  
❌ Not showing the actual output values  
❌ Forgetting to import NumPy  

✅ Show actual array values, not just code  
✅ Explain element-wise clearly  
✅ Demonstrate scalar broadcasting  
✅ Compare with list behavior  
✅ Verify shapes when needed  

---

## Pre-Recording Checklist

- [ ] Jupyter Notebook open with all cells ready
- [ ] Run all cells to verify no errors
- [ ] NumPy imported correctly
- [ ] Examples produce correct output
- [ ] Screen recording software ready
- [ ] Clear, legible font size
- [ ] Minimal distractions on screen

---

## Code Examples for Video

### Example 1: Basic Operations
```python
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
```

### Example 2: Scalar Broadcasting
```python
arr = np.array([1, 2, 3, 4, 5])

print(f"arr + 10 = {arr + 10}")
print(f"arr * 2 = {arr * 2}")
```

### Example 3: List vs Array
```python
my_list = [1, 2, 3]
my_array = np.array([1, 2, 3])

print(f"List * 2: {my_list * 2}")
print(f"Array * 2: {my_array * 2}")
```

### Example 4: Practical Use
```python
prices = np.array([100, 200, 350, 500])
discount = 0.20
final_prices = prices * (1 - discount)

print(f"Original: {prices}")
print(f"After 20% off: {final_prices}")
```

---

## Success Criteria

### Your video demonstrates:
- ✅ Element-wise operations on arrays (add, subtract, multiply, divide)
- ✅ Scalar operations on arrays
- ✅ Comparison between list and array behavior
- ✅ At least one practical example
- ✅ Understanding of shape compatibility
- ✅ Clear explanation of vectorization concept

### Your code:
- ✅ Imports NumPy correctly
- ✅ Creates arrays properly
- ✅ Shows element-wise operations
- ✅ Demonstrates scalar broadcasting
- ✅ Runs without errors
- ✅ Produces correct outputs

---

## After Recording

### Submission Checklist:
- [ ] Video is approximately 2 minutes long
- [ ] Screen is clearly visible and readable
- [ ] All code examples shown work correctly
- [ ] Element-wise operations demonstrated
- [ ] Scalar broadcasting explained
- [ ] Arrays vs lists comparison included
- [ ] Practical example shown
- [ ] Video uploaded to required platform
- [ ] Video link ready for submission
- [ ] Pull Request created (if required)

---

## Additional Notes

### Why This Milestone Matters:
- Foundation for all NumPy work
- Essential for data transformations
- Makes code more concise and readable
- Dramatically improves performance
- Used in every data science library

### Real-World Applications:
- Normalizing datasets
- Applying formulas to columns
- Scaling features for machine learning
- Financial calculations
- Scientific computing
- Image processing

### Connection to Future Milestones:
- Prepares for array aggregations
- Foundation for universal functions
- Enables boolean filtering
- Required for broadcasting understanding
- Critical for vectorized operations

---

## Quick Tips

### For Clear Demonstration:
1. Show the arrays before the operation
2. Show the operation
3. Show the result
4. Explain what happened element-by-element (at least once)

### For Better Understanding:
- Use simple, round numbers (10, 20, 30 vs 17.3, 28.9)
- Start with small arrays (3-5 elements)
- Show one concept at a time
- Build complexity gradually

### Time Management:
- Don't rush through examples
- But don't linger too long on any one concept
- Aim for smooth transitions
- Practice once before final recording

---

## Troubleshooting

### If you encounter errors:

**"NameError: name 'np' is not defined"**
→ Run the import cell first: `import numpy as np`

**"ValueError: operands could not be broadcast together"**
→ Check array shapes: `print(arr1.shape, arr2.shape)`

**"TypeError: unsupported operand type(s)"**
→ Ensure you're working with NumPy arrays, not lists

---

Good luck with your recording! 🚀
