# 410. Six-Layer Architecture

**Chapter Number:** 410
**Title:** Six-Layer Architecture
**Status:** Draft
**Version:** 0.1
**Last Reviewed:** July 3, 2026
**Depends on:** [`130_The_Problem.md`](../100_Foundations/130_The_Problem.md), [`140_CEM_Is_Not_an_AI_Framework.md`](../100_Foundations/140_CEM_Is_Not_an_AI_Framework.md)

---

# 1. Question

What are the distinct layers a piece of evidence passes through, from a candidate's raw work to a company's final decision?

---

# 2. Purpose

Two separate proposals emerged from earlier discussion of this repository: a three-layer process (Evidence Discovery, Evidence Evaluation, Decision) and a five-layer structure (Company Values, Role, Project/Team, Investigation, Human Decision). Every later Model chapter — the AI investigator's role, the Evaluation Lens, the investigation dossier — needs a single, resolved architecture to build against. This chapter provides that architecture.

---

# 3. Observation

The three-layer model was developed to solve a specific fairness problem: an open-ended, candidate-led conversation risks rewarding articulateness over capability unless judgment is kept standardized regardless of how evidence surfaces. It deliberately separated *how evidence is found* from *how evidence is judged*, so that a fixed evaluation lens could be applied consistently to unpredictable conversations.

The five-layer model was developed independently, from a different discussion, to answer a different question: what determines what a company's evaluation lens actually *contains*? It proposed that the lens itself is built from nested context — company-wide values, narrowed by the specific role, narrowed further by the specific project or team.

Neither model was built to contradict the other. They were built to answer different questions, and were never reconciled.

---

# 4. Problem

Left unreconciled, the two models create a real risk: later chapters could each build on a different one, producing inconsistent architecture across the Model section. Worse, the five-layer model's fourth layer — a single, undifferentiated "Investigation" — does not preserve the Discovery/Evaluation split that the three-layer model exists specifically to protect. Adopting the five-layer model as written would silently undo that protection.

---

# 5. Chain of Reasoning

Testing where the two models genuinely agree and where one is structurally weaker than the other:

The five-layer model's first three layers — Company Values, Role, Project/Team — describe something the three-layer model never specified: what actually constitutes a company's evaluation lens. The three-layer model simply asserted "Evaluation is standardized per company" without describing what that standard is built from. This is a real, non-duplicated contribution.

The five-layer model's fourth layer, "Investigation," is too coarse. It does not preserve the distinction between open-ended evidence gathering and standardized judgment — a distinction the three-layer model was built specifically to protect against the articulateness-reward risk (see the capture note on [Standardization vs. Depth](../9900_Capture/Standardization_vs_Depth.md)). Collapsing Discovery and Evaluation into a single "Investigation" layer would quietly reintroduce the exact fairness risk that split was designed to prevent.

The five-layer model's fifth layer, "Human Decision," matches the three-layer model's third layer, "Decision," directly. No conflict there.

The correct resolution is not to choose one model over the other. It is to combine them, keeping each model's genuine contribution and discarding the one place where a model was structurally weaker than its counterpart.

---

# 6. Conclusion

CEM's evaluation architecture has six layers, not three or five:

1. **Company Values** — the broadest context. What this organization considers important, independent of any specific role.
2. **Role** — narrows Company Values to what matters for this specific position.
3. **Project / Team** — narrows further to the immediate context the candidate would actually work within.

*(Layers 1–3 together constitute what later chapters will call the Evaluation Lens — the standardized criteria evidence gets judged against, regardless of how that evidence was found.)*

4. **Evidence Discovery** — how evidence is found. Open-ended, adaptive, candidate-led. Not standardized, and should not be.
5. **Evidence Evaluation** — how each piece of discovered evidence is judged against the lens defined by Layers 1–3. Standardized, applied identically regardless of how or when evidence surfaced in Layer 4.
6. **Human Decision** — how evaluated evidence is combined into a final recommendation or decision. Company-defined, may weight criteria differently even when the evaluation lens itself is identical.

Layers 4 and 5 remain deliberately separate. This is not a stylistic choice — it is the specific mechanism that prevents the articulateness-reward risk identified in earlier discussion. No future chapter should collapse them into a single "Investigation" step.

---

# 7. Assumptions

- **A company's evaluation lens can be fully described by three nested layers (Values, Role, Project/Team) and no more.** Untested. It is possible a real company's context requires more or fewer layers of specificity; this chapter asserts three as sufficient without testing against a real evaluation lens built end-to-end.
- **Discovery and Evaluation must remain separate to prevent the articulateness-reward risk.** Established elsewhere — this is inherited directly from the earlier Standardization vs. Depth resolution, not re-argued here.
- **Human Decision (Layer 6) is a distinct operation from Evidence Evaluation (Layer 5), not a restatement of it.** Established in this chapter's reasoning (two companies could evaluate identical evidence identically and still decide differently due to different weighting) — but not tested against a real case.

---

# 8. Supporting Evidence

**Direct observation:** This chapter's own development — two independently proposed architectures, from two separate discussions, tested against each other and found to be reconcilable rather than contradictory. This is a single internal case, not external validation.

**External research:** None cited.

**Industry signals:** None cited.

**Case studies:** None.

**Experiments:** None. No real evaluation has been run using this six-layer structure.

---

# 9. Challenges

- This chapter assumes exactly three layers of context (Company Values, Role, Project/Team) are sufficient to define an evaluation lens. A more complex organization might need more granularity (department, manager, team culture) or might find three layers already too rigid a structure to impose.
- The claim that Layers 4 and 5 "must" remain separate is inherited from an earlier resolution, not independently re-tested here. If that earlier resolution turns out to be flawed, this chapter's central structural claim inherits the flaw.
- This chapter does not yet specify how Layers 1–3 combine into a single usable evaluation lens in practice — that is deferred to a future Evaluation Lens chapter, but a reader may reasonably expect at least a proposed mechanism here.
- The six-layer model has not been tested against a real, concrete evaluation scenario end-to-end. It is a structural hypothesis, not yet demonstrated to work in practice.

---

# 10. Open Questions

- Is three layers of context (Values, Role, Project/Team) the right amount of granularity, or should this be variable per company?
- How exactly do Layers 1–3 get combined into the single evaluation lens that Layer 5 applies? (Candidate for `Evaluation_Lens.md`.)
- Should Layer 6 (Human Decision) have its own sub-structure, given that "company-defined weighting" is currently left unspecified?

---

# 11. Dependencies

[`130_The_Problem.md`](../100_Foundations/130_The_Problem.md) — this architecture exists only because 130 already established that evidence investigation is preferable to compression. Without that argument, there would be no reason to build an investigation architecture at all.

[`140_CEM_Is_Not_an_AI_Framework.md`](../100_Foundations/140_CEM_Is_Not_an_AI_Framework.md)

---

# 12. Used By

All subsequent Model chapters — [`420_The_Four_Levels_of_Evidence.md`](420_The_Four_Levels_of_Evidence.md), the AI Investigator chapter, the Company Model, Evaluation Lens, Company Values, Evidence Requirements, Investigation Dossier, and Decision Support chapters — all operate within this six-layer structure and should reference it explicitly rather than re-deriving their own architecture.

---

# 13. Revision History

- v0.1 — Initial draft. Resolves the conflict between the previously captured three-layer and five-layer proposals by combining them: adopting the five-layer model's context-nesting insight (Company Values → Role → Project/Team) while preserving the three-layer model's Discovery/Evaluation separation, which the five-layer model's single "Investigation" layer would otherwise have collapsed.

---

# 14. Status

Draft. Ready for Discussion.