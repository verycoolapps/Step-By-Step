# Examples — Gold-Standard Guides

Match the depth and tone of these. Notice what each level includes and what it omits.

## L1 — Quick (simple task)

**Task:** "How do I connect my phone to Wi-Fi?"

1. Open **Settings** → **Wi-Fi** (or **Connections → Wi-Fi** on Android).
2. Toggle Wi-Fi on and wait for networks to appear (~5s).
3. Tap your network name → type in the network key → **Connect**.
4. Verify: the network shows "Connected" and a web page loads.

*That's it — 4 steps, one checkpoint at the end, no sections for prerequisites or troubleshooting because failure here is self-evident (a mistyped network key).*


## L2 — Standard (multi-stage, everyday)

**Task:** "How do I make iced coffee at home?"

Goal: smooth, not bitter iced coffee.
Needs: coffee, cold water or milk, ice, sweetener (optional), ~10 min + optional overnight steep.

1. **Brew strong** — 1:12 coffee-to-water ratio (double strength; it dilutes with ice). French press is easiest.
2. **Cool it** — pour over a full glass of ice immediately, or refrigerate 30 min. Hot coffee on ice = watered-down.
3. **Add milk/sweetener to taste** — after dilution, so you can adjust.
4. **Verify**: balanced, not sour/watery. If watery → ratio was too weak.

Pro tip: cold-brew overnight (1:8 ratio, fridge, strain) is the low-effort path to the same result.

## L4 — Extreme detail pattern (technical task, excerpt)

Notice per-step fields and the dependency ordering. The full guide would follow the response template.

**Task:** "Deploy a static site to GitHub Pages" (beginner level)

**Phase 1 — Preparation**

**STEP 01 — Create the repository**
Goal: a public repo to host the files.
Action: go to github.com → **New** → name it (e.g., `my-site`) → keep **Public** → check "Add a README" → **Create repository**.
Location: top-right **+** → New repository.
Expected: repo page opens showing README.md.
Checkpoint: the repo URL loads and shows your repo name.
Mistake: naming it `username.github.io` unintentionally triggers special user-site behavior — fine if intended, confusing otherwise.

**STEP 02 — Add site files**
Action: click **Add file → Upload files** → drag `index.html` (and assets) → **Commit changes**.
Checkpoint: `index.html` appears in the file list.

**STEP 03 — Enable Pages**
Action: **Settings** tab → left menu **Pages** → Source: **Deploy from a branch** → Branch: `main` / `(root)` → **Save**.
Expected: a green "Your site is live at https://<user>.github.io/<repo>/" banner appears — may take 1–2 minutes.
Checkpoint: the URL loads your site. If 404, wait 2 min and hard-refresh (Ctrl+Shift+R).
Fix: if Pages settings are missing, the repo may be private — GitHub Pages on free tier requires public repos.

*(Remaining steps: custom domain, HTTPS verification, updating content — each with own checkpoints at this level.)*

## L5 — Masterclass shape (excerpt)

For "teach me Git from zero to proficient": open with the mental model (snapshots, not diffs), then 4 phases — concepts → core loop (add/commit/status/log) → branching/merging → remote collaboration — each phase ending with a practice task and a pass/fail criterion, closing with a capstone (ship a small project end-to-end) and a self-assessment checklist.
