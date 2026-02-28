# Milestone 4.20 Quick Guide: Writing Readable Variable Names and Comments (PEP 8 Basics)

## What You'll Demonstrate

Show that you can improve code readability using descriptive variable names and meaningful comments following basic PEP 8 conventions.

---

## Files for This Milestone

- `src/readable_naming_comments_demo.py` - Standalone readability demo script
- `MILESTONE_4_20_QUICK_GUIDE.md` - This walkthrough guide

---

## What the Script Covers

The script demonstrates all required milestone outcomes:

1. **Good vs poor variable names**
   - Shows why vague names (`x`, `y`, `z`) reduce clarity
   - Shows readable replacements with descriptive snake_case names

2. **Basic PEP 8 naming conventions**
   - Uses lowercase_with_underscores for variables
   - Uses uppercase for a constant value (`MAX_ALLOWED_DISCOUNT_PERCENT`)
   - Maintains naming consistency across examples

3. **Useful comments**
   - Includes comments that explain *why* logic exists
   - Avoids obvious comments that only repeat code actions

4. **Avoiding readability mistakes**
   - Avoids misleading comments
   - Avoids over-commenting simple lines
   - Keeps examples concise and review-friendly

---

## Run the Script

From project root:

```powershell
python src/readable_naming_comments_demo.py
```

If `python` is not directly available:

```powershell
C:/Users/kisho/OneDrive/Desktop/new12/.venv/Scripts/python.exe src/readable_naming_comments_demo.py
```

---

## Expected Output Highlights

You should see:

- A poor naming example with unclear variables
- A corrected readable naming example using snake_case
- A policy constant in uppercase
- An example of a comment that explains intent
- A summary of comment quality (useful vs redundant)

---

## Why This Matters

Readable code helps teams:

- Understand logic quickly during reviews
- Reduce bugs caused by ambiguous code
- Maintain and extend code safely
- Keep implementation intent clear over time

Readable code is a core professional standard.

---

## Video Recording Checklist (~2 Minutes)

### Part 1: Good vs Poor Naming (40 sec)
- [ ] Open `src/readable_naming_comments_demo.py`
- [ ] Show poor naming example (`x`, `y`, `z`)
- [ ] Show readable replacement names in snake_case
- [ ] Explain why descriptive names reduce confusion

### Part 2: PEP 8 Naming Basics (30 sec)
- [ ] Show snake_case variables
- [ ] Show uppercase constant naming
- [ ] Explain consistency across the file

### Part 3: Useful Comments (30 sec)
- [ ] Show intent-focused comment in script
- [ ] Explain why comment adds value
- [ ] Contrast with obvious/non-useful comments

### Part 4: Why Readability Matters (20 sec)
- [ ] Run script and show output
- [ ] Summarize maintainability and team review benefits

---

## Suggested 2-Minute Script

"In this milestone, I’m demonstrating readable naming and comments in `src/readable_naming_comments_demo.py`.

First, I show a poor naming example using vague variables like `x`, `y`, and `z`, and why that makes code hard to review.

Then I show a corrected version using descriptive snake_case names and an uppercase constant for policy rules.

Next, I highlight comments that explain intent, such as why a median is used, instead of obvious comments that repeat what the code already says.

Overall, readable naming and meaningful comments make code easier to understand, debug, and maintain in team projects." 

---

## Submission Checklist

- [ ] Script created in `src/`
- [ ] Script runs successfully in terminal
- [ ] Poor vs good variable naming demonstrated
- [ ] snake_case naming used consistently
- [ ] Constant naming shown where relevant
- [ ] Useful comments included (intent-focused)
- [ ] Redundant/obvious comments avoided
- [ ] ~2 minute screen video recorded and link ready
