# Response Template

Adaptive skeleton. Include a section only when it carries information the user needs; a small task gets a small answer. Section order is fixed when sections are present.

## Skeleton

```markdown
## 🚀 <Guide title — the outcome, not the topic>

**Goal:** <end state in one sentence>
**Difficulty:** <Easy / Moderate / Hard — with one-line why>
**Time:** <estimate + the assumption it depends on, or "not estimable — depends on X">
**Level:** <Beginner-friendly / assumes familiarity with Y>

### 🎯 The result we're after
<What "done" looks like. Concrete and observable.>

### 🧰 What you need
- Required: <item — why it's needed>
- Optional: <item — what it adds>
<Cost and time estimates here when relevant.>

### ⚠️ Before you start
<Hazards, irreversible actions, prerequisites, what NOT to do. Omit if genuinely nothing.>

### 📚 Steps
<numbered steps per micro-instruction format>

### 🔍 Verify
<How to confirm the whole thing worked — the observable end state.>

### 🛠️ If it goes wrong
| Symptom | Likely cause | Fix |
|---|---|---|
<3–5 most likely failures, not an exhaustive list>

### ✅ Final checklist
- [ ] <observable condition>
- [ ] <observable condition>

### 💡 Pro tip
<One technique that saves real time or prevents the most common failure.>

### ➡️ Next
<The single most relevant follow-up — deeper skill, next stage, or maintenance. Omit if the goal is fully closed.>
```

## Section rules

- **Title** names the outcome ("Get your first website live"), not the topic ("Web development").
- **What you need** separates required from optional — mixing them makes beginners buy/prepare unnecessary things.
- **Before you start** is mandatory if any step is irreversible, costs money, touches health/safety/legal, or needs a backup. Short is fine: "Back up `data/` first — Step 7 rewrites it."
- **Steps** never skip numbering and never nest more than one level deep. Phases are allowed for L4+: `Phase 1 — Preparation` as a bold line, steps numbered continuously through the whole guide.
- **If it goes wrong** is a table, 3–5 rows, only for failures with distinct causes. If troubleshooting is step-specific, put it in the step's Fix field instead.
- **Final checklist** items are observable states, not "followed the steps".
- **Pro tip** is one, concrete, and non-obvious. "Practice regularly" is not a tip.
- **Next** suggests the highest-value continuation; do not pad with "you could also learn X, Y, Z".

## Anti-patterns

- Walls of text with no structure on a multi-step task.
- A step that says "configure the settings appropriately" — name the setting or admit it's covered elsewhere.
- Checklists that check nothing ("Understand the process").
- Em-dash chains and hype adjectives; the guide should read like a calm expert wrote it.
