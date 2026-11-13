# Domain Playbooks

Per-domain traps and verification habits. Read the section matching the user's task before generating steps. These encode where guides most often fail — not domain tutorials.

## Technology & digital

- **UI paths drift.** Prefer invariant descriptions ("the blue button labeled Download") over memorized menu trees; note when paths differ across OS versions.
- **Commands**: give the exact command plus what success looks like (output line, exit behavior). Warn about destructive flags (`rm -rf`, `--force`, `DROP`).
- **Versions matter**: "works on Windows 11 / macOS 14+" beats unqualified claims. If unsure of current versions, mark UNVERIFIED.
- **Prerequisites are the #1 failure**: check tools exist (`node -v`) as an explicit early step, not an assumption.
- **Security**: never instruct disabling security features as a "fix" without explaining the risk and the safer alternative.

## Business & entrepreneurship

- **Legal/financial steps get labeled**: registration, taxes, contracts → give the general path + "verify current requirements with the official authority" — regulations change and vary by jurisdiction.
- **Costs and timelines are ESTIMATEs**: state the assumption ("for a solo founder, ~40h") and the range.
- **No invented statistics**: market sizes, success rates → UNVERIFIED with method to find them.

## Creative & design

- **Tool-agnostic where possible**: name the technique ("cut on the beat", "60-30-10 color rule") then one concrete tool path as example.
- **File specs are factual**: resolution, format, color profile → state them exactly; they are checkable.
- **Critique steps**: for iterative work (design, writing), include a review checkpoint against stated criteria, not just "export the file".

## Education & academic

- **Define terms before use** at beginner level.
- **Practice steps include the answer-check**: exercises state the success criterion ("you should get X", "if your result differs, recheck step N").
- **Citations**: if the task produces academic work, include the formatting/verification step (check page limits, required sections, citation style) rather than pretending to know the venue's rules.

## Daily life & practical

- **Safety first for tools/heat/chemicals**: PPE, ventilation, and "if X happens, do Y" before the procedure.
- **Measurements**: give both metric and the local unit context when relevant; ratios ("1 part to 2") are more reliable than absolute amounts for scaling.
- **Cleanup/closing steps count**: maintenance and storage steps are steps, not an afterthought.

## Finance & administration

- **Money steps are irreversible-adjacent**: confirm-before-submit checkpoints; never auto-advance past a payment/transfer step.
- **Deadlines and fees**: mark ESTIMATE/UNVERIFIED and name the authoritative source to confirm.
- **Privacy**: warn against entering sensitive data on unofficial sites.

## Career & professional

- **Tailoring beats templates**: guide includes "map your experience to the requirement" steps rather than a generic CV skeleton.
- **Verifiable claims only**: never coach inventing credentials, metrics, or experience.
- **Follow-up is part of the procedure**: applications/processes end with the next-action step, not "good luck".

## Health, safety & wellness

- **Scope boundary upfront**: general wellness and first-aid guidance only; diagnosis, medication, and treatment → "see a licensed professional".
- **Emergency recognition first**: for first aid, the guide leads with "when to call emergency services" before any self-care step.
- **Official-guideline priority**: cite standard bodies (e.g., national first-aid protocols, manufacturer instructions) over improvisation; mark anything beyond basics as requiring professional training.

## Universal rule

If the domain isn't listed: identify the procedure's real dependencies, the likeliest failure points, and what "done" observably means — then generate. Never refuse a domain merely because it isn't in this file.
