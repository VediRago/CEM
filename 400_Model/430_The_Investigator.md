# 430. The Investigator

**Chapter Number:** 430
**Title:** The Investigator
**Status:** Draft
**Version:** 0.3
**Last Reviewed:** July 3, 2026
**Depends on:** [`410_Six_Layer_Architecture.md`](410_Six_Layer_Architecture.md), [`420_The_Four_Levels_of_Evidence.md`](420_The_Four_Levels_of_Evidence.md)

---

# 1. Question

What, precisely, is the Investigator allowed to do inside CEM's process — and what is it never allowed to do?

---

# 2. Purpose

[`410_Six_Layer_Architecture.md`](410_Six_Layer_Architecture.md) establishes that Evidence Discovery and Evidence Evaluation are distinct layers. [`420_The_Four_Levels_of_Evidence.md`](420_The_Four_Levels_of_Evidence.md) establishes that CEM may state observations and patterns as fact, may offer interpretations only when marked as such, and must never make character judgments. Neither chapter defines who or what actually does this work. This chapter defines the Investigator's role precisely enough that later chapters (the dossier, Evidence Requirements) can build on a concrete job description rather than an implied one.

In CEM's current implementation, per [`140_CEM_Is_Not_an_AI_Framework.md`](../100_Foundations/140_CEM_Is_Not_an_AI_Framework.md), this role is performed by an AI. Nothing in this chapter's definition of the role depends on that being true — a future implementation could perform the same role differently, and this chapter should still hold.

---

# 3. Observation

Earlier discussion of this repository produced a working list of what the Investigator should do: investigate evidence, ask follow-up questions, organize findings, verify where possible, identify recurring patterns, present transparent reports. The same discussion was explicit that the investigator does not make the final decision.

That list was produced informally, before the Six-Layer Architecture and Four Levels of Evidence existed as frozen or near-frozen chapters. It has not yet been checked against either.

---

# 4. Problem

An investigator role stated only as a list of verbs ("investigate," "ask," "organize") is not yet a job description — it does not say which layer each activity belongs to, or which of the four evidence levels each activity is allowed to produce. Without that mapping, later chapters could accidentally have the Investigator perform Evidence Evaluation (which should be standardized, not conversational) inside what should be an open-ended Evidence Discovery conversation, or state a Level 3 interpretation without marking it as one.

---

# 5. Chain of Reasoning

Mapping the informal list against the architecture already established:

**Investigate evidence, ask follow-up questions** — this is Evidence Discovery (Layer 4). It is deliberately open-ended and candidate-led, per 410. The Investigator's responsibility here includes actively surfacing evidence rather than passively waiting for a candidate to volunteer it — this was the resolution to the articulateness-reward risk ([Standardization vs. Depth](../9900_Capture/Standardization_vs_Depth.md)): the burden of thoroughness sits with the Investigator, not with how well a candidate happens to narrate their own work.

**Organize findings, identify recurring patterns** — this produces Level 1 and Level 2 evidence per 420 (observations and patterns), and it can happen throughout Discovery, not only at its end.

**Verify where possible** — this is a distinct activity from both Discovery and Evaluation. Verification asks whether a claim or artifact is what it purports to be (does this document actually exist, does this prototype actually run, is this claimed authorship plausible) — not whether it's good. This is closer to a support function for Evidence Discovery than a step of Evidence Evaluation.

**Present transparent reports** — this is the output of the Investigator's work, handed to Evidence Evaluation (Layer 5) and ultimately to Human Decision (Layer 6). The report must distinguish Level 1/2 (stated as fact) from any Level 3 content (marked explicitly as interpretation), and must never include Level 4 character judgments, per 420.

**Does not make the final decision** — this confirms the Investigator's work ends at the boundary between Layer 5 (Evaluation) and Layer 6 (Human Decision). The Investigator may support Evaluation by organizing evidence against the criteria defined by Layers 1–3, but Layer 6 belongs to the human, unconditionally.

---

# 6. Conclusion

The Investigator operates within Evidence Discovery (Layer 4), with a verification function that supports it, and produces the report that Evidence Evaluation (Layer 5) consumes. Its output must be disciplined by the Four Levels of Evidence: observations and patterns stated as fact, interpretations explicitly marked as interpretations, character judgments never made.

The Investigator's defined responsibilities are:

- **Investigate** — actively explore a candidate's evidence, not passively receive it.
- **Ask follow-up questions** — probe unclear or incomplete evidence rather than accepting a first answer, with the explicit responsibility of surfacing evidence a less articulate candidate might not volunteer unprompted.
- **Verify where possible** — check whether claims and artifacts are what they purport to be, distinct from judging their quality.
- **Organize findings** — structure what has been discovered so it can be evaluated, without pre-judging it.
- **Identify recurring patterns** — elevate Level 1 observations to Level 2 patterns only when supported by multiple independent sources, per 420.
- **Present transparent reports** — output evidence with each claim's evidence level visibly marked, handed forward to Evidence Evaluation and, eventually, Human Decision.

The Investigator does not evaluate evidence against a standard (that is Layer 5's role) and does not decide (that is Layer 6's role, exclusively human).

---

# 7. Assumptions

- **A single Investigator can perform Discovery, Verification, and Reporting without those roles conflicting with each other.** Untested. It is possible that an investigator optimized for open-ended discovery is poorly suited to rigorous verification, or that combining these functions in one actor creates its own bias risk — this is not examined here.
- **"Verify where possible" is achievable at meaningful scale.** Untested. Some evidence (a working prototype, a public repository with commit history) is straightforwardly verifiable. Other evidence (a private claim about a past role or contribution) may not be verifiable by the Investigator at all — this chapter does not specify what happens when verification is not possible.
- **The Investigator can reliably distinguish Level 1/2 from Level 3 in its own output in practice**, not just in principle. Established as a requirement in [`420_The_Four_Levels_of_Evidence.md`](420_The_Four_Levels_of_Evidence.md); not yet tested against a real, generated report.

---

# 8. Supporting Evidence

**Direct observation:** This chapter's own construction — mapping an informal list of investigator activities against the already-frozen architecture and evidence-level chapters, and finding the mapping mostly consistent, with the exception of "verify" needing to be identified as a distinct function rather than folded into Discovery or Evaluation.

**External research:** None cited.

**Industry signals:** None cited.

**Case studies:** None.

**Experiments:** None. No Investigator has yet been built or tested against this role definition.

---

# 9. Challenges

- This chapter defines the Investigator's role by mapping an informal list onto existing architecture, rather than deriving the role independently from first principles. If the original informal list had gaps, this chapter may have inherited them without noticing.
- "Verify where possible" is acknowledged as having real limits (Section 7) but this chapter does not specify what the Investigator should do when verification is not possible — silently proceed, flag the evidence as unverified, or decline to use it? This is a real gap.
- The chapter does not address how the Investigator should behave if a candidate provides evidence that appears to contradict earlier evidence in the same conversation — is that itself an observation worth reporting, or does resolving contradictions belong to Evidence Evaluation?
- This chapter assumes one Investigator performs all listed functions. A future revision might reasonably ask whether Discovery and Verification should be separated into distinct roles, the same way Discovery and Evaluation were separated at the architecture level.

---

# 10. Open Questions

- What should the Investigator do when a piece of evidence cannot be verified? (Candidate for Evidence Requirements, chapter 490.)
- How should the Investigator handle contradictory evidence discovered mid-conversation?
- Should Verification eventually become its own distinct layer or role, given it doesn't cleanly belong to either Discovery or Evaluation as currently defined?
- What does a real, generated Investigator report actually look like in practice? (Candidate for the Investigation Dossier chapter, 480.)

---

# 11. Dependencies

[`410_Six_Layer_Architecture.md`](410_Six_Layer_Architecture.md)

[`420_The_Four_Levels_of_Evidence.md`](420_The_Four_Levels_of_Evidence.md)

---

# 12. Used By

[`480_The_Investigation_Dossier.md`](480_The_Investigation_Dossier.md) — defines the concrete output format this chapter's "present transparent reports" responsibility produces.

`490_Evidence_Requirements.md` — likely needs to address the verification gap this chapter identifies but does not resolve.

---

# 13. Revision History

- v0.1 — Initial draft, built from item 3 of the July 3, 2026 conversation discoveries capture, mapped explicitly against the Six-Layer Architecture and Four Levels of Evidence chapters. Identified verification as a distinct function not cleanly belonging to either Discovery or Evaluation, and flagged as an open gap rather than resolved.
- v0.2 — Renamed from "The AI Investigator" to "The Investigator," and body text genericized accordingly. The original title violated [`140_CEM_Is_Not_an_AI_Framework.md`](../100_Foundations/140_CEM_Is_Not_an_AI_Framework.md)'s own requirement that later chapters be written so they would still hold under a future non-AI implementation. Added an explicit implementation note in Section 2 instead, stating that AI performs this role currently without the role's definition depending on that fact.
- v0.3 — Fixed a broken filename reference in Used By: `480_Investigation_Dossier.md` corrected to [`480_The_Investigation_Dossier.md`](480_The_Investigation_Dossier.md), matching the file's actual name. Updated Evidence Requirements references from chapter 470 to chapter 490 to match the current Master Index placeholder.

---

# 14. Status

Draft. Ready for Discussion.