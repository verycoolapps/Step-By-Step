#!/usr/bin/env python3
"""Lint a drafted step-by-step guide (Markdown) for structural defects.

Usage:
    python lint_guide.py <guide.md> [--level 1-5]

Checks (deterministic, stdlib only):
  - Step numbering is continuous from 01/1 with no gaps or duplicates
  - No empty steps (a step with a title but no action content)
  - L3+ guides: steps lacking any verification signal (checkpoint/expected/result/verify)
  - Placeholder text left in the draft (TODO, TBD, lorem, <...> template slots)
  - "And then" chains that join two different actions inside one step (warning only)

Exit codes: 0 = clean, 1 = errors found, 2 = bad invocation.
"""
import re
import sys
from pathlib import Path

MAX_BYTES = 2 * 1024 * 1024
PLACEHOLDERS = re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum|<[a-z_ ]+>)\b", re.I)
VERIFY_HINTS = re.compile(
    r"(checkpoint|expected|verify|verifikasi|hasil yang diharapkan|cek |check that|"
    r"you should see|anda akan melihat|pastikan|confirm)",
    re.I,
)
AND_THEN = re.compile(r"\b(and then|then|setelah itu|lalu)\b", re.I)

STEP_RE = re.compile(
    r"^#{1,4}\s*(?:STEP|LANGKAH|Step|Langkah)\s*([0-9]+|[IVX]+)\b", re.M | re.I
)
NUMBERED_RE = re.compile(r"^\s*(?:[-*]\s*)?(\d{1,3})[.)]\s+(.*\S.*)\s*$", re.M)
# Multi-example files (e.g. gold-standards.md) contain several independent
# numbered lists, one per example section — reset continuity at each heading.
HEADING_RE = re.compile(r"^#{1,4}\s+\S", re.M)


def fail(msg: str) -> None:
    print(f"ERROR: {msg}")


def warn(msg: str) -> None:
    print(f"WARN:  {msg}")


def main(argv: list[str]) -> int:
    if len(argv) < 2 or len(argv) > 4 or (len(argv) == 4 and argv[2] != "--level"):
        print(__doc__)
        return 2
    path = Path(argv[1])
    level = 3
    if len(argv) == 4:
        level = int(argv[3])
    if not path.is_file() or path.is_symlink():
        print(f"ERROR: {path} is not a regular file")
        return 2
    if path.stat().st_size > MAX_BYTES:
        print(f"ERROR: {path} exceeds {MAX_BYTES // 2**20} MB")
        return 2

    text = path.read_text(encoding="utf-8", errors="strict")
    errors = 0

    # Placeholder scan
    for i, line in enumerate(text.splitlines(), 1):
        if PLACEHOLDERS.search(line):
            fail(f"line {i}: placeholder text remains: {line.strip()[:80]}")
            errors += 1

    # Step numbering
    step_nums = [int(n) for n in STEP_RE.findall(text)]

    lines = text.splitlines()
    # Positions (0-based line index) of every heading; a numbered list
    # restarts after each heading, so multi-example files stay valid.
    heading_lines = [i for i, line in enumerate(lines) if HEADING_RE.match(line)]
    numbered = []
    for m in NUMBERED_RE.finditer(text):
        line_no = text.count("\n", 0, m.start())
        numbered.append((line_no, int(m.group(1)), m.group(2)))

    if step_nums:
        expected = list(range(step_nums[0], step_nums[0] + len(step_nums)))
        if step_nums != expected:
            fail(f"STEP numbering not continuous: found {step_nums}")
            errors += 1
    elif numbered:
        runs: list[list[int]] = []
        run_headings: list[int] = []
        for line_no, n, _body in numbered:
            new_run = runs and any(
                run_headings[-1] < h < line_no for h in heading_lines
            )
            if new_run:
                runs.append([])
                run_headings.append(max(h for h in heading_lines if h < line_no))
            if not runs:
                runs.append([])
                run_headings.append(-1)
            runs[-1].append(n)
        for run in runs:
            if run != list(range(run[0], run[0] + len(run))):
                fail(f"numbered list not continuous: found {run[:20]}")
                errors += 1
    else:
        warn("no numbered steps detected — is this actually a guide?")

    # Empty steps: a step heading followed immediately by another heading.
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if STEP_RE.match(line):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and (
                STEP_RE.match(lines[j])
                or re.match(r"^#{1,4}\s", lines[j])
                or re.match(r"^\s*\d{1,3}[.)]\s+\S", lines[j])
            ):
                fail(f"line {i + 1}: empty step — '{line.strip()[:60]}' has no content")
                errors += 1

    # Numbered steps are single-line by convention; an empty body is an error.
    for _line_no, _n, body in numbered:
        if not body.strip():
            fail("empty numbered step — step has no content")
            errors += 1


    # Verification coverage at L3+
    if level >= 3 and step_nums:
        sections = re.split(r"(?m)^(#{1,4}\s*(?:STEP|LANGKAH|Step|Langkah)\s*\d+.*)$", text)
        for k in range(1, len(sections) - 1, 2):
            header, body = sections[k], sections[k + 1] if k + 1 < len(sections) else ""
            if not VERIFY_HINTS.search(body):
                warn(f"step may lack verification: '{header.strip()[:60]}'")

    # And-then chains (soft warning — sometimes legitimate)
    for i, line in enumerate(lines, 1):
        if len(AND_THEN.findall(line)) >= 2:
            warn(f"line {i}: multiple connectors in one line — consider splitting: {line.strip()[:80]}")

    if errors:
        print(f"{errors} error(s) found")
        return 1
    print("OK — guide structure is clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
