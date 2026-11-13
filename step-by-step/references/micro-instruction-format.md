# Micro-Instruction Format

How to write each step so a beginner can execute it without guessing. Not every field is required at every detail level — the table says when.

## Step anatomy

```
STEP NN — <action name, imperative>

Goal:        what this step achieves and why it exists (one line)
Action:      the exact operation, in order, one action per sentence
Location:    where it happens — menu path, button, file, tool, physical place
Detail:      the technical specifics that commonly confuse (only if non-obvious)
Expected:    what the user should observe when done right
Checkpoint:  how to verify success before moving on
Mistake:     the most common way this step fails (L3+ only)
Fix:         recovery if the checkpoint fails (L3+ only)
```

## Field rules

- **Action** is the only mandatory field. If the step is trivial ("click OK"), Action alone is fine — adding Goal to "click OK" is slop.
- **Location** is mandatory whenever the action happens inside software, a UI, a physical space, or a filesystem. "Open the settings" is incomplete; "Settings → Network → Wi-Fi" is actionable. If the exact path varies by version, give the invariant: "the section labeled Network or Connectivity".
- **Expected + Checkpoint** are mandatory at L3 and above, and for any irreversible or hard-to-verify action at any level (deleting files, payments, system changes, health-adjacent steps). A checkpoint must be observable: a message, a state change, a number, a file existing — not "it should work".
- **Goal** earns its place when the step's purpose isn't obvious from the action. "Why am I doing this?" unanswered is the #1 cause of users skipping steps.
- **Mistake/Fix** at L4–L5 and for steps with known failure modes; omit rather than invent.

## Splitting rule

If a step contains "and then", "then", "setelah itu", "lalu" joining two different locations, tools, or verifiable outcomes — split it. Test: can each half be checked independently? If yes, they are two steps.

Bad:  "Download the installer, run it, create an account, and configure the settings."
Good: four steps, each with its own checkpoint.

## Writing style inside steps

- Imperative, present tense, second person: "Open", "Select", "Wait until".
- Numbers and exact values over adjectives: "wait 30 seconds" beats "wait a moment".
- One instruction per sentence. Two instructions per sentence only when they are atomic and simultaneous ("Press Ctrl+S").
- Name the failure state when it matters: "If the button is greyed out, the prerequisite in Step 4 isn't complete."
