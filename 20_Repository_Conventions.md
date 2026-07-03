# 20. Repository Conventions

**Version:** 0.2  
**Status:** Draft

---

# Question

How should the CEM repository be organized and maintained?

---

# Purpose

This document defines the conventions used to organize, maintain, and preserve the CEM repository.

It does not define CEM itself.

It defines how the repository remains consistent, navigable, and historically traceable as the framework grows.

---

# Repository Principle — The Master Index Is the Source of Truth

The Master Index defines the conceptual architecture of CEM.

The repository mirrors that architecture.

It does not reinterpret it.

Repository organization exists to reflect the framework, not to redefine it.

If the conceptual architecture changes, the Master Index is updated first.

Only then should the repository structure change to match it.

The repository follows the framework.

It never leads it.

---

# 1. Repository Structure

The physical structure of the repository mirrors the conceptual structure of CEM.

The repository should always reflect the current Master Index.

The repository root contains only the project entry point and the top-level sections.

Example:

```text
README.md

000_Method/
    00_CEM_Development_Method.md
    10_Master_Index.md
    20_Repository_Conventions.md
    30_CEM_Development_Lifecycle.md
    90_Chapter_Blueprint.md

100_Foundations/
    110_What_is_CEM.md
    120_Origin.md
    130_The_Problem.md

200_Philosophy/

300_Core_Concepts/

400_Model/

500_Actors/

600_Experiences/

700_Architecture/

800_Ethics/

900_Research/

1000_Open_Questions/

1100_Development_Diary/

9900_Capture/
    Standardization_vs_Depth.md

History/
    README.md
```

The `000_Method/` folder contains the documents that define how CEM itself is developed and maintained.

The numbered section folders contain the framework itself and should mirror the Master Index.

The Master Index remains the single source of truth.

If the Master Index changes, the repository structure should evolve with it.

---

# 2. One Responsibility Per File

Every file answers one question.

Every folder groups files with the same responsibility.

Repository organization should never duplicate responsibility across multiple locations.

---

# 3. File Naming

Current working files keep stable names.

Example:

```text
120_Origin.md
250_Evaluation_Lens.md
```

Version numbers belong inside the file metadata.

They do not belong in active filenames.

Archived versions use versioned filenames.

Example:

```text
History/
    120_Origin/
        120_Origin_v0.1.md
        120_Origin_v0.2.md
```

This allows the current chapter to remain stable while preserving meaningful historical milestones.

---

# 4. Using the Chapter Blueprint

Every chapter must be developed using `90_Chapter_Blueprint.md`.

The blueprint is completed before prose is written.

Its purpose is to separate reasoning from presentation.

---

# 5. Capture

Ideas that arise during development but belong elsewhere should immediately move into `9900_Capture/`.

Capture exists to preserve focus.

Capture is temporary.

Nothing should remain in Capture permanently.

Every captured idea should eventually become:

- a chapter,
- part of an existing chapter,
- or be discarded after investigation.

---

# 6. Versioning

The repository always exposes one current working version of every chapter.

Meaningful previous versions are archived.

Minor edits remain documented through Git history.

Version numbers are updated inside the file.

The complete versioning workflow — including when to archive, how to update versions, and how to preserve history — is defined in `30_CEM_Development_Lifecycle.md`.

This document defines the repository convention.

The lifecycle document defines the process.

---

# 7. History

The `History/` folder preserves meaningful milestones.

Git and History serve different purposes.

Git answers:

> What changed?

History answers:

> How did this idea evolve?

Previous versions are archived before meaningful replacements.

Archived files are historical records and should not be edited except to correct archival mistakes.

---

# 8. Internal Links

Whenever files are moved or renamed, every internal reference must be updated.

Broken references should never remain in the repository.

The repository should always be internally navigable.

---

# 9. Commit Discipline

Each commit should represent one clear idea.

Avoid combining unrelated changes.

Preferred format:

```text
docs(scope): short description
```

Examples:

```text
docs(readme): introduce CEM research framework
docs(origin): add origin chapter
docs(history): archive blueprint v1.0
docs(lifecycle): refine development workflow
```

The commit history should read as the development diary of CEM.

---

# 10. Repository Evolution

Repository organization is allowed to evolve.

Structural changes should occur only when they make the repository:

- easier to understand,
- easier to navigate,
- easier to maintain,
- or more faithful to the conceptual architecture of CEM.

Repository conventions should emerge from repeated practice rather than speculation.

---

# Core Principle

The repository is not simply where CEM is stored.

It is part of the evidence.

Its organization should demonstrate the same clarity, discipline, and reasoning expected from the framework itself.
