# 485. One Investigation. Many Decisions.

**Chapter Number:** 485  
**Title:** One Investigation. Many Decisions.  
**Status:** Draft  
**Version:** 0.1  
**Last Reviewed:** July 8, 2026

---

# 1. Question

What becomes possible when CEM investigates capability and produces reusable evidence instead of a single verdict?

---

# 2. Purpose

[`210_An_ATS_Assumes_CEM_Investigates.md`](../200_Philosophy/210_An_ATS_Assumes_CEM_Investigates.md) establishes the founding distinction: an ATS assumes, while CEM investigates.

This chapter answers what follows from that distinction at the model level.

If investigation produces evidence rather than a verdict, then the same investigation can support more than one hiring question. This chapter defines that consequence so later chapters on Evaluation Lens, Evidence Evaluation, Recruiter Experience, and Human Decision do not treat each role evaluation as if it starts from zero.

---

# 3. Observation

A candidate can be a weak fit for one opening and a strong fit for another.

Current hiring workflows often treat rejection from a specific posting as the end of the relationship, even when the same candidate may contain evidence of capability relevant elsewhere in the organization.

CEM's own Investigation Dossier already preserves **Additional Observations**: evidence that may not match the immediate evaluation criteria but could be relevant beyond the current role.

---

# 4. Problem

If CEM produces rich evidence but only uses it once, it recreates one of the structural failures it exists to avoid: the candidate is still collapsed into a posting-specific outcome.

That would make investigation more expensive without fully using what investigation produces.

The problem is not only whether the current role is a fit. The problem is whether useful evidence disappears just because the first question asked of it was too narrow.

---

# 5. Assumptions

- **Investigation produces evidence that describes the candidate, not only their fit to one role.** Established by [`480_The_Investigation_Dossier.md`](480_The_Investigation_Dossier.md), especially its Findings and Additional Observations structure.
- **Evidence can be evaluated through different lenses without being recollected.** Established in this chapter as the central claim; not yet tested in a real workflow.
- **Different roles, projects, and teams can ask meaningfully different questions of the same underlying evidence.** Established conceptually by [`410_Six_Layer_Architecture.md`](410_Six_Layer_Architecture.md), which separates Evaluation Lens layers from Evidence Discovery.
- **The human decision-maker should choose which lens to apply.** Established elsewhere in the framework's human-in-the-loop logic, but not yet fully developed as its own chapter.
- **Evidence can become stale.** Currently untested in CEM; must be handled by future chapters on evidence recency, verification, and provenance.

---

# 6. Assumption Testing

- **Investigation produces evidence about the candidate beyond one role.** Partially supported by the dossier structure, but no real dossier has yet been generated and reused across multiple roles.
- **Evidence can be evaluated through different lenses.** Untested. This requires a concrete Evaluation Lens chapter and practical examples.
- **Different roles can ask different questions of the same evidence.** Partially supported by the Six-Layer Architecture, which separates lens definition from evidence discovery.
- **The human decision-maker should choose the lens.** Partially supported by the framework's existing human-decision principle, but the recruiter experience has not yet been drafted.
- **Evidence staleness matters.** Untested but likely important. A candidate's capability can change, and stored evidence should not be treated as permanent truth.

---

# 7. Chain of Reasoning

CEM investigates capability instead of assuming it from proxies.

Investigation produces evidence.

Evidence is richer than a fit score because it records what was demonstrated, how it was demonstrated, where the evidence came from, and how confident the system is in each finding.

A score can only answer the question it was computed for.

Evidence can be asked new questions because evidence describes the person more directly than a score does.

The same candidate pool can therefore be viewed through multiple lenses.

A recruiter may first apply the criteria for Role A and find that a candidate is not a strong fit. Later, the organization may open Role B, with a different lens. If the original investigation preserved the candidate's evidence, the recruiter can re-evaluate the same evidence against Role B without asking the candidate to reapply and without starting the investigation from zero.

This does not mean CEM decides that the candidate fits Role B.

It means CEM keeps the evidence visible and reusable so the human decision-maker can ask a new question of the same record.

Think of it as a spreadsheet, not a gate.

A gate produces passage or rejection. Once closed, the interaction ends.

A spreadsheet preserves underlying data. The same data can be sorted, filtered, grouped, and interpreted through different views without being recollected.

CEM should behave more like the second than the first.

---

# 8. Conclusion

CEM's investigation output should not expire the moment the first posting closes.

Because CEM produces evidence rather than a disposable verdict, one investigation can support many decisions over time. The same evidence record can be re-evaluated through different role, project, or company lenses as organizational needs change.

This is not a separate feature bolted onto CEM. It is the direct consequence of investigation producing evidence rather than a posting-specific score.

One-line version:

> Investigation produces evidence, not a verdict. Evidence is reusable, so one investigation can answer hiring questions that did not exist when the investigation was conducted.

---

# 9. Supporting Evidence

**Internal framework support:**

- [`210_An_ATS_Assumes_CEM_Investigates.md`](../200_Philosophy/210_An_ATS_Assumes_CEM_Investigates.md) establishes that CEM investigates rather than assumes.
- [`410_Six_Layer_Architecture.md`](410_Six_Layer_Architecture.md) separates Evaluation Lens definition from Evidence Discovery and Evidence Evaluation.
- [`480_The_Investigation_Dossier.md`](480_The_Investigation_Dossier.md) preserves Findings, Additional Observations, Unresolved Questions, Traceability, confidence, and verification status.

**Direct development observation:** The Dossier chapter already needed a category for Additional Observations because some evidence may be useful outside the immediate role. This chapter develops the model consequence of that category.

**External research:** None cited in this chapter.

**Experiments:** None. This principle has not yet been tested with a real candidate pool and multiple role lenses.

---

# 10. Challenges

- Evidence reuse can become unfair if old evidence is treated as permanently current. Future chapters must define recency, re-verification, and expiry rules.
- A reusable candidate evidence pool raises privacy and consent questions. Candidates may need to know whether evidence gathered for one role can be used for future roles.
- Re-sorting evidence through many lenses could overwhelm recruiters if the interface does not make the applied lens and evidence basis clear.
- The chapter assumes the same evidence can be meaningfully evaluated across roles, but some roles may require fresh evidence that was never collected in the original investigation.
- Existing ATS platforms may already support talent pools or candidate rediscovery. CEM's stronger claim should remain that its primary output is reusable evidence, not that no existing system ever stores candidates.

---

# 11. Open Questions

- What consent model is required before candidate evidence can be reused for future roles?
- How should CEM mark evidence as stale, outdated, or requiring re-verification?
- When should a new role require a fresh investigation rather than reusing an existing one?
- What should an Evaluation Lens look like in practice, and how does it operate on an existing dossier?
- How should the recruiter interface show that a candidate is a weak fit for one role but potentially strong for another?

---

# 12. Dependencies

[`210_An_ATS_Assumes_CEM_Investigates.md`](../200_Philosophy/210_An_ATS_Assumes_CEM_Investigates.md)

[`410_Six_Layer_Architecture.md`](410_Six_Layer_Architecture.md)

[`480_The_Investigation_Dossier.md`](480_The_Investigation_Dossier.md)

---

# 13. Used By

Future Evaluation Lens chapter — defines how different lenses are applied to the same evidence.

Future Recruiter Experience chapter — defines how recruiters discover and re-frame candidates across openings.

Future Human Decision / Decision Support chapter — defines how reusable evidence supports, but does not replace, human judgment.

Future Privacy / Evidence Provenance chapters — must define constraints on reusing candidate evidence over time.

---

# 14. Revision History

- v0.1 — Initial draft. Split from the broader capture note "An ATS Assumes. CEM Investigates" and positioned as a Model chapter because it describes what CEM's evidence model makes possible after investigation produces a dossier.

---

# 15. Status

Draft. Ready for Discussion.
