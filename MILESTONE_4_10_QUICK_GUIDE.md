# Milestone 4.10 Quick Guide: Writing Markdown

## What You'll Demonstrate

Show that you can write clear, professional Markdown documentation in Jupyter Notebooks using headings, lists, inline code, and code blocks.

---

## Open the Notebook

**In Jupyter (should be running at http://localhost:8889):**

1. Navigate to the `notebooks/` folder
2. Click on **`milestone_4_10_markdown.ipynb`**
3. The notebook will open

---

## Video Recording Checklist (~2 minutes)

### Part 1: Create a Markdown Cell (20 sec)
- [ ] Click below an existing cell
- [ ] Press **B** to create new cell (or use + button)
- [ ] Change cell type to **Markdown** (dropdown menu)
- [ ] Explain: "Markdown cells are for documentation"

### Part 2: Write Headings (25 sec)
- [ ] Type: `## My Analysis Section`
- [ ] Press Shift + Enter to render
- [ ] Type another heading: `### Data Loading`
- [ ] Render it
- [ ] Explain: "Headings structure the notebook"
- [ ] Show different levels: `#`, `##`, `###`

### Part 3: Create Lists (30 sec)
- [ ] Create a **bulleted list:**
  ```markdown
  - First item
  - Second item
  - Third item
  ```
- [ ] Render it
- [ ] Create a **numbered list:**
  ```markdown
  1. Step one
  2. Step two
  3. Step three
  ```
- [ ] Render it
- [ ] Explain: "Lists make steps clear and scannable"

### Part 4: Inline Code and Code Blocks (30 sec)
- [ ] Write text with inline code:
  ```markdown
  The variable `x` stores the result.
  Use the `mean()` function to calculate average.
  ```
- [ ] Render it
- [ ] Create a code block:
  ````markdown
  ```python
  import pandas as pd
  df = pd.read_csv('data.csv')
  ```
  ````
- [ ] Render it
- [ ] Explain: "Inline code references variables; code blocks show examples without execution"

### Part 5: Why It Matters (15 sec)
- [ ] "Markdown makes notebooks readable and professional"
- [ ] "Documentation helps reviewers understand your reasoning"
- [ ] "Good Markdown separates explanation from execution"

---

## Essential Markdown Syntax

### Headings
```markdown
# Heading 1 (largest)
## Heading 2
### Heading 3
#### Heading 4
```

### Lists

**Unordered (bullets):**
```markdown
- Item one
- Item two
- Item three
```

**Ordered (numbered):**
```markdown
1. First step
2. Second step
3. Third step
```

**Nested lists:**
```markdown
- Main item
  - Sub item
  - Sub item
```

### Text Formatting
```markdown
**bold text**
*italic text*
***bold and italic***
```

### Inline Code
```markdown
The variable `x` contains the result.
Use the `pandas.read_csv()` function.
```

### Code Blocks
````markdown
```python
# Your code here
import pandas as pd
df = pd.read_csv('file.csv')
```
````

### Blockquotes
```markdown
> Important note or quote
```

### Horizontal Rule
```markdown
---
```

---

## Video Script Suggestion

**Opening (5 sec):**
"In this video, I'll demonstrate writing Markdown in Jupyter Notebooks for clear documentation."

**Create Cell (15 sec):**
"First, I'll create a new Markdown cell... clicking here, pressing B for below, changing to Markdown. Markdown cells are for explanation, not execution."

**Headings (20 sec):**
"Now I'll add headings to structure the notebook. Hash symbols create headings - one hash for the largest, two for sections, three for subsections. Watch... I'll type '## My Analysis' and render it with Shift + Enter. Headings make notebooks easy to navigate."

**Lists (25 sec):**
"Let me create a bulleted list using dashes... there, that's rendered. Now a numbered list for sequential steps... one, two, three. Lists make workflows and results clear and scannable."

**Code Formatting (25 sec):**
"For inline code, I use backticks around variable names like `x` or function names like `mean()`. For longer examples, I use code blocks with triple backticks... see, this shows code without executing it. This is useful for demonstrating syntax."

**Why It Matters (15 sec):**
"Markdown transforms notebooks from code dumps into professional documents. It explains your reasoning, interprets results, and makes your work reviewable. Use Markdown before code to explain intent, and after code to interpret results."

**Closing (10 sec):**
"That's Markdown documentation - essential for clear, professional notebooks in data science."

---

## Tips for Great Markdown

### Structure Your Notebook
1. **Start with H1 title:** `# Notebook Title`
2. **Use H2 for major sections:** `## Data Loading`, `## Analysis`
3. **Use H3 for subsections:** `### Exploratory Analysis`

### Document Before and After Code
**Before Code:**
- Explain what you're about to do
- Document assumptions
- List requirements

**After Code:**
- Interpret results
- Draw conclusions
- Note observations

### Keep It Clear
- Short paragraphs
- Bullet points for multiple items
- Numbered lists for sequential steps
- Inline code for variable/function references

---

## Common Mistakes to Avoid

❌ **DON'T:**
- Write all explanations in code comments
- Skip Markdown documentation
- Use inconsistent heading levels
- Forget to render Markdown cells
- Write overly long paragraph

s

✅ **DO:**
- Use Markdown for narrative
- Document every major step
- Maintain heading hierarchy
- Always check rendered output
- Keep explanations concise

---

## Practice Exercises

### Exercise 1: Create Formatted Cell
Create a Markdown cell with:
- H2 heading: "Data Preparation"
- Short paragraph explaining purpose
- Bulleted list of 3 data sources
- Inline code reference to a variable

### Exercise 2: Document a Workflow
Create a Markdown cell with:
- H3 heading: "Analysis Steps"
- Numbered list of 5 steps
- At least 2 inline code references

### Exercise 3: Code Block Example
Create a Markdown cell with:
- Explanation paragraph
- Python code block showing example syntax
- Note about what the code does

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Render Markdown | **Shift + Enter** |
| Edit Markdown | **Double-click** or **Enter** |
| Create cell below | **B** (command mode) |
| Change to Markdown | **M** (command mode) |
| Change to Code | **Y** (command mode) |

---

## Submission Checklist

- [ ] Opened `milestone_4_10_markdown.ipynb`
- [ ] Read through all examples
- [ ] Double-clicked cells to see raw Markdown
- [ ] Created practice Markdown cells
- [ ] Recorded ~2 minute video showing:
  - Creating Markdown cells
  - Writing headings (different levels)
  - Creating lists (bulleted and numbered)
  - Using inline code and code blocks
  - Explaining why documentation matters
- [ ] Video uploaded and link ready
- [ ] Pull Request created (if required)

---

## Quick Reference Card

**Save this for future notebooks!**

```markdown
# Structure
## Major Section
### Subsection

**Bold** *Italic* `code`

- Bullet item
  - Nested item

1. Numbered item
2. Second item

> Important note

---

Inline code: `variable_name`

Code block:
```python
code here
```
```

---

## Next Steps After Video

1. Save the notebook
2. Upload video to required platform
3. Submit video link as instructed
4. Create PR with `milestone_4_10_markdown.ipynb`
5. **Use these Markdown skills in ALL future notebooks!**

**You've got this!** 🚀 Good Markdown is the difference between a code dump and a professional analysis!
