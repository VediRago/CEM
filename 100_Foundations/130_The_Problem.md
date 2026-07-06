# 130. The Problem

**Chapter Number:** 130
**Title:** The Problem
**Status:** Draft
**Version:** 0.2
**Last Reviewed:** July 3, 2026
**Depends on:** [`120 — Origin`](120_Origin.md)

---

# 1. Question

Why isn't the current approach to evaluation good enough?

---

# 2. Purpose

[`120 — Origin`](120_Origin.md) records an observation: substantial work became harder, not easier, to communicate as it grew, because evaluation relies on compressed representations of it.

That observation is autobiographical. This chapter treats it as a hypothesis and asks whether it holds beyond one person's experience.

---

# 3. Observation

The observation carried forward from Origin: as real work becomes more substantial, evaluation systems do not scale to meet it. Instead, the work is compressed into something small enough to fit the evaluator's available time — a résumé, a portfolio summary, a short interview.

This chapter asks a further question the observation implies but does not answer on its own: is this a flaw in specific evaluation tools, or a structural property of compression itself?

---

# 4. Why Summaries Exist

Summaries are not accidental. They are a real, working solution to a real constraint.

An evaluator has limited time and limited attention, and often needs to compare many candidates against each other consistently. A résumé, a portfolio summary, or a short interview solves that problem directly: it produces something small enough to review quickly, and — if structured consistently — something comparable across candidates.

Summaries are optimized for three things: **time, scale, and consistency.** They allow one evaluator to process many candidates in a bounded amount of time, using a roughly comparable format for each.

This is a real strength, not a design failure. A hiring team reviewing five hundred applications cannot investigate five hundred people's full body of work. A summary-based filter is often the only workable first pass at that scale.

---

# 5. What Summaries Necessarily Leave Behind

Every optimization has a cost. Optimizing for time, scale, and consistency has a specific, predictable cost: depth.

A summary format has a fixed size. Whatever does not fit inside that size does not survive the compression — regardless of whether it was relevant, load-bearing, or the single strongest piece of evidence a candidate had. This is not a flaw introduced by a careless candidate or a lazy evaluator. It is a structural consequence of the format itself: a fixed-size container cannot represent a variable-size body of work without loss.

The evidence that tends to be lost first is usually the evidence that is hardest to compress: reasoning, iteration, judgment under ambiguity, and the connections between separate pieces of work that only become visible when examined together. These are often among the qualities most associated with complex capability — and they are also the qualities most likely to be cut when work has to fit into a page or a ten-minute conversation.

---

# 6. Under What Conditions the Omission Becomes Significant

This loss is not always costly. For roles or evaluations where the relevant capability is itself simple, easy to state, and easy to verify quickly, a summary can capture what matters without meaningful loss.

The loss becomes significant under a specific, identifiable condition: **when the capability being evaluated is genuinely complex, and its evidence does not fit inside the size constraints of the format used to evaluate it.** This describes a large share of real hiring, admissions, and promotion decisions — cases where what actually predicts success is depth of reasoning, judgment, or process, not a checklist of discrete facts a summary can state cleanly.

---

# 7. Assumptions

This chapter's reasoning depends on the following, not all of which are established here:

- **Time, scale, and consistency are the correct, complete list of what summaries optimize for.** Untested. Named directly as a challengeable premise in Section 9 — this chapter does not verify the list is exhaustive.
- **Reasoning, iteration, and judgment-under-ambiguity are among the qualities most associated with complex capability.** Untested. This is a stated premise, not backed by cited research in this chapter — also named explicitly in Section 9.
- **A summary's fixed-size format necessarily discards content, rather than merely deprioritizing it.** Established within this chapter, Section 5 — argued as a structural, not incidental, property of fixed-size formats.
- **The generalization from Origin's single observation to a structural claim about evaluation systems is valid.** Partially established here (Sections 4–6 provide the reasoning); fully tested only insofar as the reasoning holds up to the challenges in Section 9.

---

# 8. Chain of Reasoning

*(See Sections 3–6 above, which together constitute this chapter's reasoning chain: observation → why the current approach exists → what it necessarily costs → when that cost becomes significant.)*

---

# 9. Conclusion

The issue is not that résumés, portfolios, or interviews are broken.

The issue is that they are optimized for efficient filtering under limited time and limited attention — and that optimization has a real, structural cost: it can leave important evidence of capability unavailable to the evaluator, specifically in cases where the capability being evaluated is complex enough that it does not survive compression.

This reframes Origin's personal observation as a general property of evaluation systems, not a complaint about any specific tool. The observation holds beyond one person's experience whenever the underlying condition in Section 6 is present.

---

# 10. Supporting Evidence

**Direct observation:**
- Origin's own observation (fifty days of dense, documented work becoming harder to communicate as it grew, not easier). This is the seed hypothesis this chapter tests, not independent confirmation of it.

**Industry signals:**
- The existence of a competitive AI-hiring landscape (Findem, Mokka, and others) explicitly built around the claim that "evidence-based screening" beats keyword/résumé-only screening — a signal that this problem is recognized industry-wide, not invented for this framework. This is directional evidence, not verified research.
- The SHRM 2026 finding that "the hiring process has become a black box," and a recruiter's own quote: "They don't care so much about your potential. They want real-time proof." (see `9900_Capture/` research notes, if formalized there.) Sourced from trade reporting, not peer-reviewed research — treated accordingly as a weaker, directional signal.

**External research:** None cited in this chapter. This is a genuine gap — no peer-reviewed or rigorously sourced research is yet cited to support Sections 5–6's central claims.

**Case studies:** None.

**Experiments:** None. CEM has not yet tested its own claims empirically.

**External validation:** None.

---

# 11. Challenges

- This chapter argues from a constraint-and-tradeoff framing rather than a "summaries are bad" framing specifically to remain defensible — but that framing could itself be challenged: is "time, scale, and consistency" really the correct list of what summaries optimize for, or is it incomplete?
- Section 5's claim that reasoning, iteration, and judgment-under-ambiguity are "often among the qualities most associated with complex capability" is currently unsupported by any cited research or evidence. It is stated as a reasonable premise, not a proven one, and should either be backed by evidence in a later revision or held explicitly as an open assumption.
- Section 6's condition ("when capability is complex enough that it does not survive compression") is stated qualitatively, not with any measurable threshold. This is a real gap: without a way to identify in advance when the condition applies, the chapter's claim is harder to test or falsify.
- This chapter does not yet address whether an AI-mediated alternative (CEM's actual proposed mechanism) avoids the same tradeoff or merely relocates it — that question belongs to later Model chapters, but the reader may reasonably expect it to be raised here.
- (Added on migration) No External Research is cited anywhere in this chapter's Supporting Evidence — every source is either the founding personal observation or trade-press-level industry signal. Until peer-reviewed or rigorously sourced research is added, this chapter's central claim rests on weaker evidentiary footing than its confident tone might suggest.

---

# 12. Open Questions

- Can the condition in Section 6 be made more precise — some way to identify, in advance, whether a given role or evaluation is at high risk of this specific failure?
- Does CEM's own mechanism (AI-led investigation) introduce a new, different tradeoff of its own, in the same way summaries trade completeness for scale? (Candidate for a future Ethics or Model chapter.)

---

# 13. Dependencies

[`120 — Origin`](120_Origin.md)

---

# 14. Used By

Later Model and Evaluation Lens chapters, which propose CEM's mechanism as a response to the problem established here.

---

# 15. Revision History

- v0.1 — Initial draft. Observation through Conclusion established, along with an initial unified Supporting Evidence list and Challenges.
- v0.2 — Migrated to Blueprint v1.2 compliance. Added Metadata block. Added Assumptions section (four identified, each marked established/untested with source). Retyped Supporting Evidence into six categories per the evidence-typing fix discovered in [`9900 — Capture Typed Evidence`](../9900_Capture/Typed_Evidence.md) — this made visible a real gap: no External Research is currently cited anywhere in this chapter, only direct observation and industry signals. Added a corresponding Challenges item naming that gap explicitly. No change to Observation, Problem, Chain of Reasoning, or Conclusion content.
- v0.3 — Removed the redundant "This chapter answers" metadata field, since Section 1 (Question) already carries this information. Later chapters use only "Depends on" in metadata, with the actual question stated once, in Section 1.

---

# 16. Status

Draft. Ready for Discussion.