# Milestone 4.15 Quick Guide: Working with Python Lists, Tuples, and Dictionaries

## What You'll Demonstrate

Show that you can create and use Python’s core collection types, understand mutability vs immutability, and choose the right structure for simple problems.

---

## Files for This Milestone

- `src/collections_demo.py` - Standalone collections demo script
- `MILESTONE_4_15_QUICK_GUIDE.md` - This walkthrough guide

---

## What the Script Covers

The script demonstrates all milestone requirements with simple, intentional examples:

1. **Lists (ordered, mutable)**
   - Create a list with multiple values
   - Access values using indexes
   - Modify an element
   - Add and remove values
   - Iterate through list items

2. **Tuples (ordered, immutable)**
   - Create a tuple with fixed values
   - Access tuple values by index
   - Observe immutability using a controlled `TypeError` example

3. **Dictionaries (key-value pairs)**
   - Create a dictionary with meaningful keys
   - Access values using keys
   - Update an existing key
   - Add a new key-value pair

4. **Choosing the right structure**
   - List: changing sequences
   - Tuple: protected fixed values
   - Dictionary: named fields / structured entities

---

## Run the Script

From project root:

```powershell
python src/collections_demo.py
```

If `python` is not directly available:

```powershell
C:/Users/kisho/OneDrive/Desktop/new35/.venv/Scripts/python.exe src/collections_demo.py
```

---

## Expected Output Highlights

You should see:

- List operations (`index`, assignment, `append`, `remove`, iteration)
- Tuple index access and a tuple immutability `TypeError`
- Dictionary key access, update, and insertion
- A final summary on when to use each structure

---

## Why This Matters

Using the right collection type improves code quality:

- Better organization of related values
- Fewer access and mutation bugs
- Cleaner and more readable logic
- Easier maintenance and extension

Collections are core tools for structuring data in Python.

---

## Video Recording Checklist (~2 Minutes)

### Part 1: List Example and Operations (35 sec)
- [ ] Open `src/collections_demo.py`
- [ ] Point out list creation
- [ ] Show index access (`0`, `-1`)
- [ ] Show list modification, `append`, and `remove`
- [ ] Mention lists are mutable

### Part 2: Tuple Example and Immutability (30 sec)
- [ ] Show tuple creation and indexed access
- [ ] Run script and point to tuple `TypeError`
- [ ] Explain tuples are immutable (cannot be changed)
- [ ] Mention tuples are good for fixed values

### Part 3: Dictionary Example (30 sec)
- [ ] Show key-value dictionary creation
- [ ] Show access by key
- [ ] Show updating existing key and adding new key
- [ ] Explain dictionaries model real-world entities

### Part 4: Difference and Use Cases (25 sec)
- [ ] Explain list vs tuple vs dictionary in one summary
- [ ] Mention choosing based on behavior needed
- [ ] State why right structure reduces errors

---

## Suggested 2-Minute Script

"In this milestone, I’m demonstrating Python lists, tuples, and dictionaries using a standalone script in `src/collections_demo.py`.

First, lists: I create a list, access items by index, modify values, append new items, remove items, and iterate through the list. This shows lists are ordered and mutable.

Second, tuples: I create a tuple and access values by index. Then I show what happens when trying to modify a tuple. Python raises a TypeError because tuples are immutable.

Third, dictionaries: I create key-value data, access values by key, update an existing key, and add a new key. This is useful for structured, named data.

In summary: use lists for changing sequences, tuples for fixed values, and dictionaries for labeled fields. Choosing the right structure makes Python code clearer and safer." 

---

## Submission Checklist

- [ ] Script created in `src/`
- [ ] Script runs successfully in terminal
- [ ] List operations demonstrated and explained
- [ ] Tuple immutability demonstrated and explained
- [ ] Dictionary key-value access and updates demonstrated
- [ ] Use-case differences explained clearly
- [ ] ~2 minute screen video recorded and link ready
