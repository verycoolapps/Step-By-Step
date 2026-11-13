# Quality Gates

Internal audit run on every generated guide before delivery. A gate fails → fix the guide; never ship and apologize. These complement the user-visible sections — they check the guide, not the reader.

## Completeness gate

- [ ] The user's actual goal is stated, not just their literal question.
- [ ] Every required prerequisite appears in "What you need" — including knowledge prerequisites for beginners ("you'll need to know what a BIOS is" → link/explain or add a step).
- [ ] Steps are ordered by real dependency; nothing used in step N requires something introduced in step N+1.
- [ ] Each phase/step has an observable expected result or checkpoint at L3+.
- [ ] The final state is defined concretely ("site live at URL", "file exports without errors").

## Actionability gate

- [ ] Every step is executable by the stated user level — no step assumes unexplained knowledge.
- [ ] Every software/UI step names where it happens (menu path, button label, file path) or explicitly acknowledges version variance.
- [ ] No step contains two actions in different locations joined by "and then" unless atomic.
- [ ] Commands are exact and copy-pasteable; destructive flags are called out.
- [ ] Time/duration expectations are stated where the user would otherwise think it hung ("wait ~60s", "first launch takes a few minutes").

## Accuracy gate

- [ ] No invented proper nouns: menu names, button labels, commands, URLs, prices, version numbers, regulations.
- [ ] Volatile facts (current versions, prices, policies, laws) are verified with available tools or labeled UNVERIFIED with a named authority to check.
- [ ] Estimates carry their assumption ("~2h for a beginner" not "2h").
- [ ] Platform/version scope is stated; "works everywhere" claims are replaced with the actual supported range.

## Safety gate

- [ ] Every irreversible or risky action (delete, overwrite, payment, reset, electrical, chemical, health-adjacent) is flagged before it happens, not after.
- [ ] Data-loss steps have a backup instruction first.
- [ ] Licensed-professional domains (medical diagnosis, legal filing, structural/electrical work) are scoped to guidance + professional referral.
- [ ] Security-weakening steps (disabling firewall/AV, sharing credentials) include the risk and a safer alternative.

## Anti-slop gate

- [ ] No filler openings ("Great question!", "Absolutely!") or sign-offs ("Hope this helps!").
- [ ] No step exists only to look thorough — every step changes state or produces a checkable result.
- [ ] No repeated explanations; each concept is defined once.
- [ ] No decorative checklists ("Understand the process ✓").
- [ ] Length matches the detail level — L1 stays short; padding at L1 is a defect.
- [ ] Personality is calm-expert: helpful, direct, no hype adjectives.

## Failure-path gate

- [ ] The troubleshooting table covers the 3–5 most likely failures for this specific task — not generic ones.
- [ ] At least one recovery path exists per risky step.
- [ ] The guide states what to do if the user's environment differs from the assumed one.
