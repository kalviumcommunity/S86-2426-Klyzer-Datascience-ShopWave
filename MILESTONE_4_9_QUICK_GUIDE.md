# Milestone 4.9 Quick Guide: Kernel Management

## What You'll Demonstrate

Show that you understand how to run, restart, and interrupt Jupyter kernels safely and know when to use each action.

---

## Open the Notebook

**In Jupyter (should still be running at http://localhost:8889):**

1. Navigate to the `notebooks/` folder
2. Click on **`milestone_4_9_kernels.ipynb`**
3. The notebook will open

---

## Video Recording Checklist (~2 minutes)

### Part 1: Running Cells Normally (30 sec)
- [ ] Show running cells in sequence (Shift + Enter)
- [ ] Point out the kernel indicator (circle in top-right)
- [ ] Explain: "The kernel remembers variables between cells"
- [ ] Run a few cells that build on each other

### Part 2: Interrupt Execution (30 sec)
- [ ] Scroll to the long-running countdown cell
- [ ] Run it and watch it start counting
- [ ] Explain: "This is taking too long, I'll interrupt it"
- [ ] Click **Kernel → Interrupt** (or use the stop button)
- [ ] Show the KeyboardInterrupt error
- [ ] Explain: "Interrupt stops execution but keeps variables"

### Part 3: Restart Kernel (45 sec)
- [ ] Explain: "Now I'll restart to clear all variables"
- [ ] Click **Kernel → Restart** (confirm the dialog)
- [ ] Run the test cell that checks if `x` exists
- [ ] Show it fails with NameError (expected!)
- [ ] Explain: "After restart, all variables are cleared"
- [ ] Optionally show **Restart & Run All**

### Part 4: Explain When to Use Each (15 sec)
- [ ] "Use **Interrupt** when code takes too long or gets stuck"
- [ ] "Use **Restart** to get a clean slate or test reproducibility"
- [ ] "Always **Restart & Run All** before submitting work"

---

## Key Actions to Demonstrate

### 1. Running Cells
- Press **Shift + Enter** to run a cell
- Watch the kernel indicator turn busy (filled circle)
- See output appear below the cell

### 2. Interrupting
**Menu:** `Kernel → Interrupt`

**Button:** Click the **■ (stop)** button in toolbar

**Keyboard:** Press **I, I** (I key twice in command mode)

### 3. Restarting
**Options:**
- `Kernel → Restart` - Clears memory, keeps output
- `Kernel → Restart & Clear Output` - Clears memory and all output
- `Kernel → Restart & Run All` - Restarts and runs all cells top to bottom

---

## Video Script Suggestion

**Opening (5 sec):**
"In this video, I'll demonstrate Jupyter kernel management - running, interrupting, and restarting."

**Running Cells (25 sec):**
"First, I'll run these cells in sequence. Notice how the kernel remembers variables - x is defined here, then used here. The filled circle shows the kernel is busy."

**Interrupting (25 sec):**
"Now I'll run this countdown cell... it's taking too long, so I'll interrupt it using Kernel → Interrupt. There we go - you see the KeyboardInterrupt error. The execution stopped, but variables are still in memory."

**Restarting (35 sec):**
"Now I'll restart the kernel to clear everything. Watch - I'm clicking Kernel → Restart... confirmed. Now when I run this test cell, x is undefined because the kernel was reset. To verify the notebook works, I'll do Restart & Run All... and everything executes from top to bottom."

**When to Use (15 sec):**
"Use Interrupt when code takes too long. Use Restart to test reproducibility or clear stale variables. Always Restart & Run All before submitting. This ensures your notebook works cleanly."

**Closing (10 sec):**
"That's kernel management - essential for debugging and reproducible notebooks."

---

## Important Kernel States

| Indicator | State | Meaning |
|-----------|-------|---------|
| ⚪ Empty circle | Idle | Ready to execute |
| ⚫ Filled circle | Busy | Currently executing code |
| `In [*]` | Running | This cell is executing |
| `In [5]` | Complete | This cell was executed (number 5) |

---

## Common Kernel Issues & Solutions

| Problem | Solution |
|---------|----------|
| Cell running too long | **Interrupt** (Kernel → Interrupt) |
| Infinite loop | **Interrupt** (Kernel → Interrupt) |
| Variables have wrong values | **Restart** (Kernel → Restart) |
| Cells ran out of order | **Restart & Run All** |
| Need to test reproducibility | **Restart & Run All** |
| Notebook appears frozen | **Interrupt** first, then Restart if needed |

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Run cell | **Shift + Enter** |
| Interrupt kernel | **I, I** (press I twice) |
| Restart kernel | **0, 0** (press 0 twice) |

*Note: Shortcuts work in command mode (press Esc to enter command mode)*

---

## Best Practices to Mention

✅ **DO:**
- Always run cells top to bottom
- Restart & Run All before final submission
- Interrupt instead of closing the tab when stuck
- Check kernel indicator to see if code is running

❌ **DON'T:**
- Run cells in random order
- Submit notebooks without testing "Restart & Run All"
- Close browser when a cell is stuck (interrupt instead!)
- Forget to clear output before sharing

---

## Submission Checklist

- [ ] Opened `milestone_4_9_kernels.ipynb`
- [ ] Practiced running cells in sequence
- [ ] Interrupted a long-running cell
- [ ] Restarted the kernel
- [ ] Tested "Restart & Run All"
- [ ] Recorded ~2 minute video
- [ ] Video uploaded and link ready
- [ ] Pull Request created (if required)

---

## Tips for Recording

1. **Start with a fresh kernel restart** before recording
2. **Narrate what you're doing** as you click
3. **Show the kernel indicator** changing states
4. **Demonstrate the countdown interrupt** - it's visual and clear
5. **Show the test cell failing after restart** - proves variables cleared
6. **End with Restart & Run All** - shows everything works

---

## Next Steps After Video

1. Save the notebook
2. Upload video to required platform  
3. Submit video link as instructed
4. Create PR with `milestone_4_9_kernels.ipynb`

**You've got this!** 🚀 Understanding kernels prevents 90% of notebook debugging issues!
