# CEM Development Method

**Version:** 1.0  
**Status:** Frozen  
**Frozen On:** 2026-07-03

---

## Purpose

This repository documents the research and development of the Capability Evidence Model (CEM).

Its purpose is not to defend an idea.

Its purpose is to discover whether the idea is true.

CEM is developed through structured reasoning, evidence, and iteration.

---

## Core Principle

The framework is not designed.

It is discovered.

Each chapter should emerge from previous reasoning rather than being invented in advance.

---

## Development Rules

### Rule 1 — One Chapter, One Question

Every chapter answers exactly one question.

Examples:

- What is CEM?
- Why does CEM exist?
- What is capability?
- What is evidence?

If a discussion answers multiple questions, split it.

---

### Rule 2 — Chapters Are Written In Isolation

Only one chapter is developed at a time.

While writing a chapter:

- Ignore unfinished chapters.
- Ignore future implementation.
- Ignore unrelated ideas.

Focus only on the current question.

---

### Rule 3 — The Repository Is The Memory

The repository stores completed reasoning.

Discussions should not attempt to remember previous work by default.

Once reasoning is documented, it leaves the conversation and becomes part of the repository.

The repository becomes the project's source of truth.

**Exception:** A frozen chapter may be deliberately brought back into active discussion only when required by **Rule 8 — Challenge the Framework**.

This is not a violation of Rule 3.

It is the only sanctioned reason to reintroduce completed reasoning into active development.

When the challenge is resolved, the chapter must be:

- **Reaffirmed** — the existing reasoning still holds.
- **Revised** — the reasoning changes while preserving the chapter.
- **Replaced** — the previous reasoning is no longer valid and is superseded.

Once resolved, the chapter returns to the repository and once again becomes the source of truth.

---

### Rule 4 — Capture Before Context Switching

If a new idea appears during discussion:

1. Capture it.
2. Place it in the appropriate chapter or Capture folder.
3. Return immediately to the current discussion.

Never interrupt a chapter to develop another one.

---

### Rule 5 — Every File Has One Responsibility

A file should answer one question only.

If multiple independent concepts exist, they become separate files.

---

### Rule 6 — Stable Numbering

Files use permanent decimal numbering.

Example:

```text
110_What_is_CEM.md
120_Origin.md
130_The_Problem.md
```

If a new chapter belongs between two existing chapters:

```text
125_New_Concept.md
```

Existing files are never renumbered.

---

### Rule 7 — Evidence Over Opinion

Ideas are not accepted because they sound convincing.

Every significant conclusion should be supported by:

- reasoning,
- research,
- observation,
- or evidence.

---

### Rule 8 — Challenge The Framework

The goal is not to prove CEM.

The goal is to challenge it.

Contradictions strengthen the framework when resolved.

---

### Rule 9 — CEM Must Obey CEM

The framework itself should satisfy the same principles it asks others to follow.

Its evolution should be:

- transparent,
- traceable,
- explainable,
- and evidence-based.

---

## Chapter Lifecycle

```text
Draft
↓
Discussion
↓
Revision
↓
Approved
↓
Frozen
```

A frozen chapter is only reopened when new evidence or contradictions require it.

---

## Chapter Template

```text
Status:

Question:

Purpose:

Depends On:

Used By:

Open Questions:
```

---

## Final Principle

Do not write the framework.

Discover it.
