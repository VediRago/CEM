# 20. Repository Conventions

**Version:** 0.1  
**Status:** Draft

---

# Purpose

This document explains how CEM repository documents should be created, structured, revised, versioned, and archived.

It does not define CEM itself.

It defines how the repository preserves the development of CEM in a consistent, inspectable way.

---

# 1. Use the Chapter Blueprint Before Writing

Every CEM chapter must follow `90_Chapter_Blueprint.md`.

The blueprint is not optional.

Before writing a chapter as prose, first fill the blueprint sections:

1. Question
2. Purpose
3. Observation
4. Problem
5. Assumptions
6. Assumption Testing
7. Chain of Reasoning
8. Conclusion
9. Supporting Evidence
10. Challenges
11. Open Questions
12. Dependencies
13. Used By
14. Revision History
15. Status

The purpose is to separate thinking from writing.

A chapter should not become polished prose before its reasoning structure is clear.

---

# 2. One Chapter, One Question

Every chapter answers one question only.

If a discussion produces more than one question, the ideas must be split into separate files or moved into Capture.

A chapter should not answer another chapter's question.

---

# 3. Chapter Development Workflow

A chapter moves through the following workflow:

```text
Draft
↓
Discussion
↓
Testing
↓
Revision
↓
Approved
↓
Frozen
```

A chapter should not be frozen until:

- its assumptions are visible,
- its reasoning is shown,
- its conclusion is limited to what the reasoning supports,
- its challenges are documented,
- and unresolved questions are recorded.

---

# 4. Versioning Rule

Current working files keep their stable chapter filename.

Example:

```text
90_Chapter_Blueprint.md
120_Origin.md
```

Version numbers live inside the file metadata.

Example:

```text
Version: 1.1
Status: Frozen
```

The filename should not change every time the document changes.

The current file always represents the current working version.

---

# 5. When To Archive A Version

A previous version should be archived when a document reaches a meaningful milestone or undergoes a substantial conceptual change.

Archive when:

- a frozen version is replaced by a new version,
- a major reasoning structure changes,
- a concept is reframed,
- a chapter moves from one stable version to another,
- or the previous version is useful for understanding how the idea evolved.

Do not archive every minor wording change.

Minor edits are preserved by Git history.

The History folder is for meaningful reasoning milestones.

---

# 6. How To Archive A Version

Archived versions go inside `History/` using this structure:

```text
History/
  Chapter_Name/
    Chapter_Name_v1.0.md
    Chapter_Name_v1.1.md
```

Example:

```text
History/90_Chapter_Blueprint/
  90_Chapter_Blueprint_v1.0.md
```

The archived file should preserve the version exactly as it existed at that milestone.

Archived files are historical records.

They should not be edited casually.

---

# 7. Updating A Current File After Archiving

When a new version replaces an older milestone:

1. Archive the older meaningful version in `History/`.
2. Update the current file in its normal location.
3. Update the file metadata.
4. Add a revision history entry explaining the change.
5. Commit with a message that makes the reason clear.

Example commit messages:

```text
docs(history): archive chapter blueprint v1.0
docs(blueprint): update chapter blueprint to v1.1
```

---

# 8. Git History vs History Folder

Git history remains the authoritative version history.

The `History/` folder exists for a different reason.

It makes important reasoning milestones visible without requiring someone to inspect the Git log.

Git preserves every change.

History preserves meaningful conceptual stages.

Both matter.

---

# 9. Capture Folder Rule

If an idea appears during work on another chapter and does not belong there, move it to `9900_Capture/` or its proper future chapter.

Do not derail the active chapter.

Capture exists to protect focus.

Nothing should remain in Capture permanently.

---

# 10. Commit Discipline

Each commit should have one clear purpose.

Avoid commits that combine unrelated changes.

Preferred commit style:

```text
docs(scope): short description
```

Examples:

```text
docs(readme): introduce CEM research framework
docs(origin): add initial origin chapter draft
docs(history): establish version archive structure
docs(conventions): add blueprint and versioning workflow
```

The Git history should read like the development diary of CEM.

---

# 11. Core Repository Principle

The repository is not only where CEM is stored.

It is where CEM proves how it was developed.

The evolution of reasoning is itself evidence.
