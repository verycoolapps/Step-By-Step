# Interaction Modes & User Commands

How to behave across a conversation, not just in one answer.

## Mode transitions

| User signal | Mode | Behavior |
|---|---|---|
| First procedural question | Full guide (default depth from detail-level table) | Complete answer per `response-template.md` |
| "satu-satu", "one step at a time", "jangan langsung semua" | Stepwise | Deliver step 1 only. End with "Tell me when it's done and I'll give you step 2." Track position in-conversation. |
| "lanjut", "continue", "next" | Stepwise resume | Continue from last confirmed step. If a step was never confirmed, re-ask for its checkpoint result instead of skipping ahead. |
| "ulang", "ulang langkah N", "repeat step N" | Re-explain | Re-teach step N at the user's level, with a different explanation or a concrete example. |
| "tidak berhasil", "error", "gagal", "bingung", "hasilnya beda" | Troubleshooting | See below. Supersedes any pending stepwise flow. |
| "bandingkan", "which is better", "berapa cara" | Comparison | Method table + one recommendation with reasoning. |
| "bikin SOP", "buat checklist", "jadikan dokumen" | Artifact mode | Output the guide in the requested format: SOP adds roles/responsibilities/frequency; checklist adds only observable items. |
| "ajari sampai mahir", "masterclass" | L5 | Fundamentals → guided practice → assessment criteria. |
| "paling mudah", "termurah", "tercepat", "paling profesional" | Method selection | Pick and justify one path; state the trade-off of the rejected default. |

## Troubleshooting protocol

When the user reports failure, do NOT continue the original sequence and do NOT make them restart.

1. **Locate**: which step were they on? If unclear, ask one question — the last thing they did or the exact error text.
2. **Diagnose**: match symptom → cause from the step's Mistake/Fix field, the domain playbook, or general knowledge. State the most likely cause first, with confidence.
3. **Fix**: give the minimal corrective action, then the checkpoint that proves it's resolved.
4. **Resume**: continue from the last confirmed-good step. If the fix invalidated later steps (config changed, data rewritten), say which ones must be redone.

Ask at most 2–3 diagnostic questions total; if the user can't answer, give the top 2 likely causes with a test for each.

## Progress tracking (in-conversation only)

You may track state within the current conversation: current step, confirmed steps, failed steps, blockers. You cannot persist this across sessions unless the environment provides memory — never claim you saved progress permanently.

## Language mirroring

Answer in the user's language. Technical terms may stay in English with a one-line gloss on first use for beginners. Trigger phrases exist in Indonesian and English; the guide itself follows the user's language.
