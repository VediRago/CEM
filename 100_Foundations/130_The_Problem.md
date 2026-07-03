# 130. The Problem

**Status:** Draft
**Depends on:** `120_Origin.md`
**This chapter answers:** Does the observation in Origin describe a real, general problem — or just one person's experience?

---

# 1. Question

Why isn't the current approach to evaluation good enough?

---

# 2. Purpose

`120_Origin.md` records an observation: substantial work became harder, not easier, to communicate as it grew, because evaluation relies on compressed representations of it.

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

# 7. Conclusion

The issue is not that résumés, portfolios, or interviews are broken.

The issue is that they are optimized for efficient filtering under limited time and limited attention — and that optimization has a real, structural cost: it can leave important evidence of capability unavailable to the evaluator, specifically in cases where the capability being evaluated is complex enough that it does not survive compression.

This reframes Origin's personal observation as a general property of evaluation systems, not a complaint about any specific tool. The observation holds beyond one person's experience whenever the underlying condition in Section 6 is present.

---

# 8. Supporting Evidence

- Origin's own observation (fifty days of dense, documented work becoming harder to communicate as it grew, not easier).
- The existence of a competitive AI-hiring landscape (Findem, Mokka, and others) explicitly built around the claim that "evidence-based screening" beats keyword/résumé-only screening — an independent signal that this problem is recognized, not invented for this framework.
- The SHRM 2026 finding that "the hiring process has become a black box," and a recruiter's own quote: "They don't care so much about your potential. They want real-time proof." (see `9900_Capture/` research notes, if formalized there.)

---

# 9. Challenges

- This chapter argues from a constraint-and-tradeoff framing rather than a "summaries are bad" framing specifically to remain defensible — but that framing could itself be challenged: is "time, scale, and consistency" really the correct list of what summaries optimize for, or is it incomplete?
- Section 5's claim that reasoning, iteration, and judgment-under-ambiguity are "often among the qualities most associated with complex capability" is currently unsupported by any cited research or evidence. It is stated as a reasonable premise, not a proven one, and should either be backed by evidence in a later revision or held explicitly as an open assumption.
- Section 6's condition ("when capability is complex enough that it does not survive compression") is stated qualitatively, not with any measurable threshold. This is a real gap: without a way to identify in advance when the condition applies, the chapter's claim is harder to test or falsify.
- This chapter does not yet address whether an AI-mediated alternative (CEM's actual proposed mechanism) avoids the same tradeoff or merely relocates it — that question belongs to later Model chapters, but the reader may reasonably expect it to be raised here.

---

# 10. Open Questions

- Can the condition in Section 6 be made more precise — some way to identify, in advance, whether a given role or evaluation is at high risk of this specific failure?
- Does CEM's own mechanism (AI-led investigation) introduce a new, different tradeoff of its own, in the same way summaries trade completeness for scale? (Candidate for a future Ethics or Model chapter.)

---

# 11. Dependencies

`120_Origin.md`

# 12. Used By

Later Model and Evaluation Lens chapters, which propose CEM's mechanism as a response to the problem established here.
