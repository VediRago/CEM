# 330. Confidence

**Chapter Number:** 330
**Title:** Confidence
**Status:** Draft
**Version:** 0.3
**Last Reviewed:** July 3, 2026
**Depends on:** `420_The_Four_Levels_of_Evidence.md`, `480_The_Investigation_Dossier.md`

---

# 1. Question

What does confidence mean in CEM, and how is it determined?

---

# 2. Purpose

Confidence has appeared, undefined, in four separate chapters: `130_The_Problem.md` (implicitly, in the reliability of a single observation), `420_The_Four_Levels_of_Evidence.md` (implicitly, in the distinction between what can and cannot be stated as fact), `430_The_Investigator.md` (as an assumption not yet tested), and `480_The_Investigation_Dossier.md` (explicitly, as a per-finding property with an unresolved scale). This recurrence across four chapters, none of which formally defined the concept, is itself the evidence that Confidence needed its own chapter — consistent with this repository's own discipline of building structure only once real pressure for it exists, not speculatively.

---

# 3. Observation

Across the chapters where Confidence appeared, a consistent shape recurred without ever being named as a rule: confidence was never proposed as a single, dossier-wide number. Every prior mention attached confidence to something specific — a specific claim, a specific pattern, a specific finding — and every prior mention connected confidence, at least loosely, to how much independent supporting evidence stood behind that specific thing.

---

# 4. Problem

Without a formal definition, "confidence" risks being used inconsistently across future chapters — sometimes meaning "how certain is this claim," sometimes "how much evidence supports this," sometimes "how likely is this to be true" — three related but distinct ideas that a term used loosely can blur together. `480` already needed confidence to do real work (attaching it to Findings) without ever defining what it actually measures.

---

# 5. Chain of Reasoning

Confidence in CEM cannot mean the same thing it might mean in ordinary conversation — a general sense of certainty — because CEM's own Four Levels (per `420`) already separate different kinds of claims with different epistemic status. An Observation (Level 1) is directly verifiable; a Pattern (Level 2) is inferred from repetition. These cannot share one undifferentiated notion of confidence, because what confidence would even *represent* is different in each case.

For an Observation, confidence should represent something close to verification status — was this directly confirmed, or reported and unconfirmed. This is a narrower, more binary-leaning question than confidence in a Pattern.

For a Pattern, confidence should represent the strength of the inference from repetition — how many independent sources support it, how genuinely independent those sources are from each other, and whether any evidence contradicts the pattern. This is a broader, more graduated question than confidence in a single Observation.

This means Confidence is not one concept with two applications — it is defined differently depending on which evidence level it attaches to, and a chapter that tried to define a single universal confidence scale across both levels would be forcing two different questions into one number, obscuring rather than clarifying what the number means.

`480`'s open question — what is the actual relationship between source count and confidence for a Pattern — can be partially answered here, though not fully resolved. A Pattern built from the minimum number of sources required to count as a pattern at all (per `420`, more than one) should carry lower confidence than the same pattern supported by many independent sources. But "how much lower" cannot be reduced to a fixed formula without testing against real cases — the relationship is directional, not yet quantified.

---

# 6. Conclusion

Confidence in CEM is not a single, universal measure. It takes a different form depending on the evidence level it attaches to:

- **Observation-level confidence** represents verification status: directly confirmed, reported but unconfirmed, or unable to verify (per the Verification gap already flagged in `430_The_Investigator.md`).
- **Pattern-level confidence** represents the strength of an inference from repetition: it should scale with the number of independent supporting sources, and should account for whether those sources are genuinely independent of each other or share a common origin that would make them count as one source in practice.

Confidence should never be expressed as a single dossier-wide score (consistent with `480`'s existing design), and should never be used to imply a claim is more certain than the evidence level it belongs to allows — a high-confidence Pattern is still a Pattern (Level 2), never elevated to the certainty of a directly verified Observation (Level 1) regardless of how many sources support it.

---

# 7. Assumptions

- **Confidence genuinely needs to be defined differently per evidence level, rather than as one scale with different inputs.** Established as this chapter's central claim; not tested against an alternative design where a single scale with level-aware weighting might work equally well.
- **Source independence can be reliably assessed** (i.e., that CEM, or its Investigator, can actually tell whether two supporting observations are genuinely independent or secretly share a common origin). Untested — this chapter assumes the assessment is possible without specifying how it would be done in practice.
- **A directional relationship (more sources → more confidence) is sufficient without a precise formula.** This chapter deliberately stops short of quantifying the relationship, on the assumption that premature quantification would be speculative rather than evidence-based. This may prove insufficient once real dossiers are generated and evaluators need an actual number to act on.

---

# 8. Supporting Evidence

**Direct observation:** The recurrence of Confidence, undefined, across four separate chapters (130, 420, 430, 480) — itself the primary evidence that this chapter was needed, and the basis for this chapter's central distinction (Observation-confidence vs. Pattern-confidence), which was extracted from how the term was already being used inconsistently across those four chapters.

**External research:** None cited. This is a genuine gap — concepts like confidence intervals, source triangulation, and inter-rater reliability exist in established research fields (statistics, journalism, intelligence analysis) and could meaningfully inform this chapter, but none are cited here.

**Industry signals:** None cited.

**Case studies:** None.

**Experiments:** None. No real dossier has yet been generated to test whether this two-tier confidence design is usable in practice.

---

# 9. Challenges

- This chapter's central design choice — different confidence definitions per evidence level — adds real complexity. A simpler, unified model might be easier for a human evaluator to actually use, even if slightly less precise. This chapter does not test that tradeoff.
- Source independence is treated as assessable but the chapter does not specify how. Two pieces of evidence that appear independent (two different documents, two different conversations) could still share a hidden common origin (the same underlying claim, restated) that a naive count would miss.
- This chapter explicitly avoids quantifying the source-count-to-confidence relationship, which leaves `480`'s original open question only partially resolved — directionally answered, not operationally answered. A future evaluator building a real implementation will still need to make that quantification decision without guidance from this chapter.
- This chapter does not address confidence for Level 3 interpretations at all, even though `420` permits interpretations to be offered when marked. If interpretations can vary in how well-supported they are, this chapter's framework may need extending to cover that case too.

---

# 10. Open Questions

- What is the actual quantitative relationship between source count and Pattern-level confidence? (Deferred, not resolved, from `480`.)
- How should source independence actually be assessed in practice?
- Should Level 3 interpretations also carry a confidence designation, and if so, does it need its own definition distinct from both Observation- and Pattern-level confidence?
- Is there a single, more general principle underlying both definitions in this chapter — something like "confidence measures how justified a claim is within its own evidence level," where Observation-confidence (justified by verification) and Pattern-confidence (justified by independent repetition) are two implementations of one idea, rather than two separate concepts? This chapter currently has evidence for two of the three cases such a principle would need to unify — Level 1 and Level 2 — and no evidence yet for Level 3, whose justification mechanism (explanatory power? consistency? something else?) has not been defined anywhere in this repository. Until Level 3 exists, this chapter cannot honestly claim to have found a unifying principle; it can only note that one might exist. If Level 3 confidence, once defined, turns out to be justified by a mechanism that fits the same higher-level pattern, this chapter's two-tier definition should be revised into that single, more general principle. If it doesn't fit, the hypothesis is rejected and the two-tier definition stands as correct on its own terms. Either outcome is evidence-driven, which is the point of leaving this open rather than resolving it now.
- Does external research on confidence intervals, source triangulation, or inter-rater reliability offer a more rigorous foundation than this chapter's current reasoning-only approach?

---

# 11. Dependencies

`420_The_Four_Levels_of_Evidence.md`

`480_The_Investigation_Dossier.md`

---

# 12. Used By

`480_The_Investigation_Dossier.md` should be revisited once this chapter is stable, to confirm its existing Confidence field matches this chapter's two-tier definition rather than the less specific placeholder treatment it currently has.

Future `470_Evidence_Requirements.md` and Evaluation Lens chapters, which will need to weigh findings partly by their confidence.

---

# 13. Revision History

- v0.1 — Initial draft. Built in response to Confidence's undefined recurrence across four chapters (130, 420, 430, 480), directly addressing the deferred scale/threshold question from `480`'s Open Questions. Established a two-tier definition (Observation-level = verification status, Pattern-level = strength of inference from repetition) rather than a single universal scale, and left the actual quantitative relationship between source count and confidence as an open question rather than speculating on a formula without evidence.
- v0.2 — Added a flagged hypothesis to Open Questions: the two-tier definition may itself be two implementations of one deeper principle ("confidence measures how justified a claim is within its own evidence level"). Deliberately not adopted in this version, since only two of the three evidence-level cases this abstraction would need to unify currently exist — Level 3's justification mechanism is not yet defined. Revisit once Level 3 confidence is addressed.
- v0.3 — Sharpened the same Open Question with a clearer three-case framing (Level 1 and Level 2 have evidence, Level 3 does not yet exist), and made explicit that either outcome once Level 3 is defined — the hypothesis fitting or not fitting — counts as evidence-driven progress, not a failure either way.

---

# 14. Status

Draft. Ready for Discussion.
