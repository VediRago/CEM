# 480. The Investigation Dossier

**Chapter Number:** 480
**Title:** The Investigation Dossier
**Status:** Draft
**Version:** 0.3
**Last Reviewed:** July 3, 2026
**Depends on:** `410_Six_Layer_Architecture.md`, `420_The_Four_Levels_of_Evidence.md`, `430_The_Investigator.md`

---

# 1. Question

What does the Investigator's output actually contain, and how is it structured?

---

# 2. Purpose

`430_The_Investigator.md` establishes that the Investigator's final responsibility is to "present transparent reports," but does not define what such a report actually contains or how it is structured. This chapter defines that output — the Investigation Dossier — precisely enough that Evidence Evaluation (Layer 5) and Human Decision (Layer 6) have a concrete, consistent artifact to work from, rather than an unstructured account of a conversation.

---

# 3. Observation

Earlier discussion of this repository proposed that the Investigator's output should be "richer than a score" — containing Evidence, Observations, Confidence, Unresolved questions, Patterns, Verification, and Additional observations. That list was produced informally, before the Six-Layer Architecture and Four Levels of Evidence existed as settled chapters, and has not yet been checked against either.

---

# 4. Problem

A report that mixes evidence, pattern, interpretation, and uncertainty together — without visibly labeling which is which — would violate `420_The_Four_Levels_of_Evidence.md` even if every individual claim inside it was properly leveled. The four-level discipline has to survive not just at the level of a single sentence, but at the level of the document format itself. Without a defined structure, that discipline could be quietly lost in the transition from conversation to report.

---

# 5. Chain of Reasoning

Mapping the informally proposed dossier contents against the architecture and evidence-level chapters already established:

**Evidence and Observations** correspond directly to Level 1 in `420`. These should be the most numerous, most concrete entries in the dossier — specific, verifiable things that were said, shown, or demonstrated. In the dossier's structure, these are Findings of type Observation.

**Patterns** correspond to Level 2 — but per `420`, a pattern requires repetition across independent sources, not a single instance. The dossier must therefore be able to show its work: a stated pattern should be traceable back to the multiple observations that support it, not asserted on its own. In the dossier's structure, these are Findings of type Pattern — not a separate category from Observation, but a second tier within the same category, since both are levels of evidence rather than fundamentally different kinds of content.

**Additional observations** — evidence that doesn't map to the specific criteria being evaluated for this role, but may be relevant elsewhere in the organization (per earlier discussion, item 19). This is a legitimate dossier category distinct from the main findings, since it serves Human Decision differently — it's informational, not part of the primary recommendation.

**Confidence** is a new concept not yet defined anywhere in this repository. It cannot simply be a single overall number — per `420`, different claims in the same dossier will sit at different evidence levels, and a Level 2 pattern supported by five independent sources deserves more confidence than a Level 1 observation with none. Confidence should therefore attach to individual findings, not to the dossier as a whole.

**Unresolved questions** are distinct from Confidence — a low-confidence finding is still a finding; an unresolved question is something the Investigator was unable to determine at all, and should be reported as an honest gap rather than papered over or given a false confidence score.

**Verification** was already identified in `430` as a function that does not cleanly belong to Discovery or Evaluation. In the dossier, verification status should attach to individual pieces of evidence (verified / unverified / unable to verify) rather than existing as its own separate section — this keeps the open architectural question (does Verification deserve its own layer) from being silently pre-answered by the dossier's format.

**What the dossier must never contain**, per `420`: any Level 4 character judgment. No claim of the form "the candidate is [trait]" belongs anywhere in this document, regardless of confidence level.

---

# 6. Conclusion

The Investigation Dossier is a structured document, not a narrative account of the conversation that produced it. Its primary content is a set of **Findings**, where each Finding is either an Observation (Level 1) or a Pattern (Level 2) — not two separate categories, but two tiers within the same category, consistent with `420_The_Four_Levels_of_Evidence.md`. Each Finding carries its own confidence and verification status rather than the dossier receiving a single overall score.

Beyond Findings, the dossier separately reports Unresolved Questions (gaps the Investigator could not determine, distinct from low confidence) and Additional Observations (relevant evidence outside the immediate evaluation criteria, kept structurally separate since it serves Human Decision differently than the primary findings).

The dossier may contain Level 3 interpretation only when it is explicitly identified as interpretation. It never contains Level 4 character judgment under any circumstance.

The dossier's job is to hand Evidence Evaluation (Layer 5) something that can be judged against a company's criteria without Evaluation having to first untangle what is fact, what is pattern, what is guesswork, and what is missing.

## Canonical Structure

```
INVESTIGATION DOSSIER

1. Investigation Metadata
   - Candidate / subject identifier
   - Date, scope, role or context being evaluated
   - Investigator version / implementation

2. Findings
   Each Finding contains:
   - Type: Observation (Level 1) or Pattern (Level 2)
   - Statement: the finding, stated at its appropriate evidence level (Observation or Pattern) and never beyond what the supporting evidence justifies
   - Supporting evidence: for a Pattern, the independent
     observations it is built from; for an Observation,
     the specific artifact or moment it comes from
   - Confidence: attached to this Finding specifically
   - Verification status: verified / unverified / unable to verify

3. Additional Observations
   - Findings relevant beyond the immediate evaluation
     criteria, kept structurally separate from Section 2

4. Unresolved Questions
   - What the Investigator was unable to determine,
     reported as an honest gap, not a low-confidence guess

5. Traceability
   - Links or references back to the original evidence
     (documents, artifacts, conversation excerpts) for
     every Finding, so any claim in the dossier can be
     checked against its source
```

Any Level 3 interpretation offered anywhere in the dossier must be visibly marked as interpretation, distinct from the Findings structure above — it is never itself a Finding.

---

# 7. Assumptions

- **Confidence can be meaningfully attached to individual findings rather than expressed as a single overall score.** Established as this chapter's central design choice; not yet tested against a real generated dossier.
- **Verification status can be recorded per piece of evidence without resolving whether Verification deserves its own architectural layer.** This is a deliberate hedge — the dossier format is designed to work regardless of how that open question in `430` is eventually resolved.
- **"Additional observations" (evidence relevant outside the immediate role) is worth including as a standing category, not just an occasional aside.** Untested — this is inherited from item 19 of the source discussion and not independently re-argued here.

---

# 8. Supporting Evidence

**Direct observation:** This chapter's own construction — mapping an informally proposed content list against the architecture, evidence-level, and Investigator chapters, and finding most of it consistent, with Confidence requiring a genuinely new design decision (per-finding rather than dossier-wide) not present in the original informal list.

**External research:** None cited.

**Industry signals:** None cited.

**Case studies:** None.

**Experiments:** None. No dossier has actually been generated from a real investigation yet.

---

# 9. Challenges

- Per-finding confidence is more complex to design and to read than a single overall score, and this chapter does not test whether a human evaluator can actually use a dossier structured this way efficiently, or whether it overwhelms Layer 6 with more granularity than a real decision-maker can act on.
- This chapter does not specify how many independent sources are required before an observation is allowed to become a stated pattern — the same open question already flagged in `130_The_Problem.md`, unresolved here as well.
- "Unable to verify" is listed as a legitimate status, but this chapter does not specify how Evidence Evaluation (Layer 5) should weigh an unverifiable claim — treat it as absent, treat it neutrally, or treat it with suspicion? This is a real gap, deferred to a future Evaluation Lens chapter.
- The dossier format assumes findings can be cleanly separated from each other. Real evidence may be more entangled — a single piece of work might support multiple patterns simultaneously, and this chapter does not address how the dossier should represent that overlap without becoming redundant or confusing.

---

# 10. Open Questions

- Can a human evaluator actually use a dossier with per-finding confidence efficiently, or does it need to be summarized further for Layer 6 while preserving full detail for anyone who wants to check it?
- How should Evidence Evaluation weigh a finding marked "unable to verify"?
- How should the dossier represent a single piece of evidence that supports multiple, separate patterns?
- Traceability (Section 5 of the canonical structure) may be a bigger principle than this chapter — "every finding must be traceable back to its supporting evidence" could plausibly belong as a core CEM concept referenced from multiple chapters, not just a section within the dossier. Not resolved here; worth revisiting once more chapters exist to check whether the same need for traceability recurs elsewhere.

---

# 11. Dependencies

`410_Six_Layer_Architecture.md`

`420_The_Four_Levels_of_Evidence.md`

`430_The_Investigator.md`

---

# 12. Used By

Future Evaluation Lens chapter — consumes the dossier as its primary input.

Future Decision Support chapter — the dossier is what Layer 6 (Human Decision) ultimately reviews.

---

# 13. Revision History

- v0.1 — Initial draft, built from item 20 of the July 3, 2026 conversation discoveries capture, mapped explicitly against the Six-Layer Architecture, Four Levels of Evidence, and Investigator chapters. Introduced per-finding confidence and verification status as a genuinely new design decision not present in the original informal proposal, specifically to remain consistent with `420`'s requirement that different evidence levels carry different epistemic weight.
- v0.2 — Restructured Findings so Observation and Pattern are two tiers within one category (Finding), rather than two separate parallel categories — this had been an unintentional inconsistency with Section 5's own reasoning, which already treated Pattern as Level 2 within the same evidence hierarchy as Observation's Level 1. Added a canonical dossier structure (Investigation Metadata, Findings, Additional Observations, Unresolved Questions, Traceability) so the chapter shows the actual artifact rather than only its governing rules.
- v0.3 — Fixed the Statement field wording, which had said findings are "stated as fact" uniformly — this failed to preserve the distinction between Observation (genuinely factual) and Pattern (a fact about a pattern's existence, but bounded by what supporting evidence justifies). Flagged Traceability as a possible future core CEM principle in Open Questions, without expanding scope to formalize it as its own chapter yet.

---

# 14. Status

Draft. Ready for Discussion.
