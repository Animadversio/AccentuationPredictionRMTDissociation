# Page-limit trim proposal (2026-09-25)

ICLR 2026 allows **9 pages** of main text at submission (10 for camera-ready). The current `main_body_compact.tex` runs about 30 lines onto p.10: the end of Sec. 6 plus the whole Discussion.

The proposal lives in a **copy**; the original is untouched:
- `main_body_compact_trimmed.tex`: the edited main text.
- `accentuation_rmt_main_compact_trimmed.tex`: the driver, identical to `accentuation_rmt_main_compact_draft.tex` except that it inputs the trimmed body.

**Result:** the main text ends at line 481 of p.9, where p.9 holds lines 432–485, so 4 lines are to spare. No undefined references. No numbers were changed; issue #2 is left to Binxu.

Tag legend:
- **W**: a widow line (a short last line of a paragraph) is removed.
- **C**: condensed wording.
- **Cap**: caption trimmed.
- **!**: changes content or claims, so review it.

| Tag | Where | Change | Kind |
|---|---|---|---|
| T1 | Abstract, opening | Two sentences merged; grammar fixed ("that, models"; "associated by"). | C |
| T2 | Abstract, last sentence | "predicts the variation of in vivo control capability of models better than…" becomes "orders models' in vivo control better than held-out accuracy". | C |
| T3 | Contribution (ii) | "cross-validation in anisotropic data and teacher leaves…" becomes "…leaves a computable residual control error under anisotropic data". | C |
| T4 | End of contributions | "All results are proved in the appendix, which restates them…; each is validated by MC and natural-image regression". Fixes "we also restates". | W |
| T5 | Fig. 1 caption | The design sentence duplicated the Sec. 2 text; replaced by a pointer. | Cap |
| T6 | Fig. 1 caption | "Details: Apps. B.6, B.2." | Cap, W |
| T7 | Sec. 2 opening paragraph | Shorter appendix pointer; "Three observations stand out." | W |
| T8 | Sec. 2 closing paragraph | Rewritten from 5 lines to 3.5. **!** It now says the good controller differs "only slightly and along less extreme [low-variance] directions". The original "weight error more along the high eigenspace" was wrong: w₁'s perturbation lies in eigenvectors ranked d−499 to d−100 with norm 1 (B.2). | C, W, ! |
| T9 | Sec. 3 "Teacher and student" | "$\hat\beta=F^\top\hat w$ is the effective pixel weight, i.e. $\nabla_x f$". | W |
| T10 | Table 1 caption | Geometry details dropped (the text lists them right after). **!** The Pearson remark is dropped too, since it is in App. C. | Cap, W |
| T11 | Fig. 2 (wrapfig) caption | Shorter. **!** It also fixes issues #22/#23: "prediction-optimal penalty" instead of "cross-validation", and "noise-averaged path" instead of "mean Ridge path". | Cap, ! |
| T12 | Sec. 4 opening | Two sentences become one. | W |
| T13 | "The ridge path…" paragraph | Last sentence merged. | C |
| T14 | Toolkit | κ definition compacted; the "DE allows us…" sentence was dropped as redundant. | C |
| T15 | Toolkit | Norm-inflation sentence condensed, with the Sec. 5/6 pointers merged. | C |
| T16 | Fig. 3 caption | A–C condensed; the MC-validation sentence became a parenthesis. | Cap |
| T17–18 | Reading of Prop. 1 | Dropped "The two control moments have a plain reading." and "The second term of D is the key issue."; the df₁,₂ clause is tighter. | C |
| T19 | Kernel discussion | **!** The red κ-sensitivity sentence was removed. Suggest moving it to App. `rem:app-tuning-remarks`. | C, ! |
| T20 | Kernel discussion | Tightened; "(slope_acc = 1/(1+z) < 1)" became "(slope_acc < 1)". | W |
| T21 | Landscape paragraph | 4 sentences become 3. | C |
| T22 | "This answers the question in the title…" | Condensed. | C, W |
| T23 | Peer review, neural stats | Rewritten as one clean sentence with the same numbers. | C |
| T24 | Peer review, symmetry note | **!** 3 lines become 1: symmetric in pixel space, asymmetric across feature maps (App. J.5). The "recognize its own noise" mechanism is left to the appendix. | C, ! |
| T25 | Fig. 4 caption | Pointers merged. | Cap |
| T26 | Gauge paragraph | The two white-data remarks merged into one sentence. | C |
| T27 | Summary box, last lines | One sentence; the `\cite{?}` is kept. | C |
| T28 | Fig. 5 caption | 9 lines become about 6. The A/B/C/D descriptions and subset legend were compressed; the commented-out text remains. | Cap |
| T29 | Sec. 6, first paragraph | "Exact for linear φ; theory-motivated diagnostic for networks"; the smoothing sentence was shortened. | C, W |
| T30 | Sec. 6 results | **!** The caveats "descriptive… model ordering… teacher-dependent terms" moved to Limitations (T32). | C, ! |
| T31 | Discussion | Condensed. | C |
| T32 | Limitations | Takes the caveats from T30; "DEs" instead of "deterministic equivalents". | C, W |

## Reserve cuts
Use these if the pending main-text fixes add lines, e.g. #2 numbers or #6 PCA750:
- Inline the $B_{p,q}$ / $\mathrm{df}_{p,q}$ display in Sec. 4 (about 2 lines).
- Merge the three bold geometry items (ellipsoids / spheres / hyperplanes) in Sec. 3 into one sentence, since Table 1 has the column (about 2 lines).
- Compress Related work (about 1–2 lines).
- Shrink Fig. 1 to `0.95\linewidth` (about 2 lines).

## Not touched
- The `\todo{History…}` in the Introduction.
- The main-text issues #1, #2, #3, #6 and #8 (see the issue tracker).
