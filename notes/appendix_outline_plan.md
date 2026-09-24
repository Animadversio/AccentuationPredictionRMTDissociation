# Appendix outline plan (draft for review, 2026-09-24)

## Decisions (Binxu, 2026-09-24)
- Order: **Extended results (A) → Methods (B) → Theory (C–L)**. Wired in `accentuation_rmt_main_compact_draft.tex`.
- The null-rotation figure (`fig:app-null-rotation`) **moved to A.3**. Theory `sec:app-gauge-fragility` now points to it.
- The full dependency graph (`fig:summary_stats_dep_graph`) **stays in theory**. The main-text Fig. 4 caption points to it.
- Q3 toy-model code: **found** — `Closed-loop-visual-insilico/scripts/accentuation_theory/exp2_accentuation.py` (outputs in `$STORE_DIR/DL_Projects/AdvExampleLinearRegr/exp2/`). Details are in the B.2 comments of `extended_methods.tex`.
- Q4 models: data and model definitions come from upstream `jacob-prince/parametric-neural-control` (branch jacob) and local `~/Github/Closed-loop-visual-insilico`. Binxu recalls the data came from BrainScore and that the robust model is L∞ ε = 8. **To verify**: see B.6 / B.7.
- Q5 per-model spectra: use a common df₂ = 375 and generate the panels separately first; layout decided later.
- Q6: decide later.
- **Structure and linking first; no plotting until the structure is settled.** Figures not yet exported show as `\suppfigplaceholder{source path}` boxes.
- Main-text issues (bottom of this file) are archived; Binxu will fix them.

## Figure status (2026-09-24, pass 1: copy existing)
- 16 existing figures were copied to `figures/supp/` and wired into A.1–A.5 with draft captions. Each figure environment keeps its `CR/...` source path in a comment.
- **Still NEW (placeholders):** `fig:supp-neural-self-vs-peer` (A.4) and `fig:supp-model-spectra` (A.5, per-model PC-resolved spectra at df₂ = 375).
- Interim for the per-model figure: `fig:supp-model-energy` (the `model_exact_energy_bars` figure).
- The methods-validation figures sit at the end of A.5: `fig:supp-affine-calibration` and `fig:supp-stein-validation`. Methods B.6 / B.8 can reference these labels.
- **To fix:**
  - The geometry legend shows a literal `68\%`.
  - Crop rows G–I from the DE-vs-MC composite.
  - Check the caption of the encoding-session benchmark.
  - `session_endpoint_image_bootstrap.png` was left out: its sign (+0.1) conflicts with the neighborhood correlation figure (−0.28).
- `\clearpage` at the end of `extended_results.tex` keeps all A floats before B. A spans pp. 14–25.

## Structure status (2026-09-24)
- New `extended_results.tex` (A.1–A.5) and `extended_methods.tex` (B.1–B.11), with section labels, figure labels and placeholder boxes.
- `appendix_vanhateren_landscape_methods.tex` was demoted to a subsection and is now B.4 (label unchanged).
- Main-text links were added: Fig. 1 → B.6 / B.2; Sec. 2 → B.6 / B.7; Fig. 2 → A.1; Fig. 3 → B.4 / A.2 (fixed `suppfig:pixl-MC` and the empty `\ref{}`); peer stats → A.4 / B.9; Fig. 4 → full graph / B.5 / A.3; "random draws" → `fig:supp-null-random`; Sec. 6 → B.8; Fig. 5 → A.5.
- The build has 0 undefined references. Local build needs the shim `.sty` files and must drop `adjustbox` / `cancel`, which are unused.

### Label map
| Part | Label |
|---|---|
| A | `sec:app-extended-results` |
| A.1 | `sec:app-ext-geometry` · `fig:supp-ridge-path-geometry` |
| A.2 | `sec:app-ext-pixel` · `fig:supp-pixel-de-mc`, `fig:supp-pixel-slope`, `fig:supp-pixel-selection`, (`fig:supp-synthetic-validation`, Q6) |
| A.3 | `sec:app-ext-gauge` · `fig:app-null-rotation`, `fig:supp-null-random`, `fig:supp-null-row-spectra`, `fig:supp-null-dimension` |
| A.4 | `sec:app-ext-peer` · `fig:supp-neural-peer-matrix`, `fig:supp-neural-self-vs-peer` |
| A.5 | `sec:app-ext-nonlinear` · `fig:supp-model-spectra`, `fig:supp-nonlinear-benchmark`, `fig:supp-smoothing-scale`, `fig:supp-nonlinear-robustness` |
| B | `sec:app-methods` |
| B.1 | `sec:app-methods-images` |
| B.2 | `sec:app-methods-toy` |
| B.3 | `sec:app-methods-geometry` |
| B.4 | `sec:app-vanhateren-landscape-methods` |
| B.5 | `sec:app-methods-feature` |
| B.6 | `sec:app-methods-neural-data` |
| B.7 | `sec:app-methods-models` · `tab:app-models` |
| B.8 | `sec:app-methods-nonlinear` |
| B.9 | `sec:app-methods-peer` |
| B.10 | `sec:app-methods-stats` |
| B.11 | `sec:app-methods-compute` |

---

Legend: ✅ exists, just insert | 🔧 exists, needs re-export / crop / fix | 🆕 needs new plot or computation | ✍️ needs writing
Code repo = `~/Github/AccentuationPredRMT` (abbrev. `CR/`). Paper repo = this directory.

Proposed appendix order (in `accentuation_rmt_main_compact_draft.tex`):

```
\appendix \tableofcontents
\input{extended_results}      % A  Extended figures / results
\input{extended_methods}      % B  Detailed methods (absorbs appendix_vanhateren_landscape_methods.tex)
\input{theory_appendix_polished}   % C...  Theory (roadmap, main results, proofs, RMT toolkit)
```

---

## A. Extended results (supplementary figures)

### A.1 Geometry of the ridge path (supports Fig. 2 / Sec. 3–4)
- **Fig. S1** `CR/figures/geometry/ridge_paths_iso_error_geometry.{pdf,png}` 🔧
  - (a) fixed λ, σ² varied: Gaussian ellipses of β̂ | X are concentric and grow with σ.
  - (b) fixed σ², λ varied: mean path, 68% ellipses, prediction-stationary point vs z=0 control point.
  - Fix: the legend shows a literal `68\%`; the "teacher β*" label overlaps; drop the suptitle.
  - Alternatives: `_emphasis`, `_thin_background`, `_lambda_only`.
- Optional: `iso_error_geometry_overlay_eps001/004` 🔧, showing that ε→0 makes the dissociation extreme (Exp. `ex:mr-dissociation`).
- Text ✍️: 1 short paragraph linking this to Prop. `mr-iso-geometry`.

### A.2 Pixel-ridge landscape: extra views (supports Fig. 3)
- **Fig. S2 = missing `suppfig:pixl-MC`**: DE vs natural-image MC for E_gen, E_acc and R²_acc.
  - Source: `CR/figures/vanhateren_landscape/export/composite/paper_composite_three_landscapes_de_mc_rows_figexport.pdf` ✅/🔧
  - Rows G–I duplicate main Fig. 3, so crop to the 2×3 heatmaps.
- **Fig. S3** slope landscape: slope_gen and slope_acc, DE and MC.
  - Source: `CR/figures/vanhateren_landscape/landscape_slope_kappa.png` ✅/🔧
  - Could be merged into S2 as a 4th column.
- **Fig. S4** fixed penalty vs CV-selected vs E_acc-oracle along the noise axis, for E/S, R², slope and κ.
  - Source: `CR/notebooks/outputs/pixel_ridge/vanhateren_selection_estimation/selection_vs_estimation_extended_with_sklearn_cv.png` ✅
  - Also shows leading DE vs the Gaussian surrogate. This is the evidence for "leading DE fails near the control optimum" (App. ratio corrections).
- Optional **Fig. S5** synthetic check: isotropic / power-law R²_gen, R²_acc, R²_peer; DE vs MC, with delta correction.
  - Source: `CR/figures/peer_validation/r2_peer_validation.png` ✅
  - Supports Prop. mr-peer and the claim that "isotropic ⇒ CV gives control for free".
  - Also `CR/figures/model_selection/cv_selected_r2.png` (real K-fold CV vs DE-selected).
- Optional: the van Hateren spectrum s_k plus disk-teacher power b_k² per PC 🆕 (small).
  - Data: `CR/tables/vanhateren_spectral_teacher_profile.csv`, `vanhateren_disk_teacher_spectrum.npz`.
  - It visualizes "anisotropic spectrum + structured teacher". It could also go in Methods B.1.

### A.3 Feature ridge: dependency graph and gauge family (supports Fig. 4)
- Dependency graph: **already in theory App. G.1** (`fig:summary_stats_dep_graph`, `feature_summary_statistics_flow_SigmaF`). Decide whether to move it here or leave it (see open questions).
- Null-rotation family: **already in App. G.3** (`fig:app-null-rotation`, Top500 + Top100).
- New additions:
  - **Fig. S6** random draws in the prediction-null family (p=500).
    - Source: `CR/figures/null_rotations/vanhateren_p500_random_null_diversity.pdf` ✅
    - E_gen and R²_gen are identical; E_acc, R²_acc and slope span orders of magnitude.
    - This is the evidence for the main-text sentence "random draws from the rotation group span a huge range".
  - **Fig. S7** what the rotation does to feature rows: per-row spectral energy over population PC rank at t = 0, 1e-4, 1e-2, 1.
    - Source: `vanhateren_top_pc_tail_feature_spectra.pdf` ✅
  - **Fig. S8** dependence on feature dimension p (16, 128, 500, 1000): leading DE vs Gaussian distributional DE vs MC.
    - Source: `vanhateren_null_dimension_curves.pdf` ✅
  - Optional: DE-selected α vs empirical CV, T_F vs DE/MC.
    - Source: `null_rotations/export/top500_final/empirical_cv_backup/top500_empirical_cv_tf_vs_de_mc.pdf` 🔧

### A.4 Neural peer review (supports Sec. 2 and the peer paragraph of Sec. 4)
- **Fig. S9** 10×10 generator × reviewer matrices of MSE, r, identity R² and slope (diagonal boxed; mean over 25 sites).
  - Source: `CR/figures/nonlinear_control/neural_peer_review/peer_review_four_metrics_jacob_order.pdf` ✅
- 🆕 panel: self vs peer distributions (R², slope; strip or box plot) with test statistics. The stats already exist in `PEER_REVIEW_SELF_VS_PEER_RESULTS.md`:
  - Peer vs self: slope 1.35 [1.14, 1.59] vs 0.38 [0.33, 0.42].
  - All 10 self slopes are < 1; 80 of 90 peer slopes are > 1.
  - Permutation p < 5e-6; subject sign-flip p = 0.0625.

### A.5 Nonlinear diagnostic: full comparison and robustness (supports Fig. 5)
- **Fig. S10** full predictor benchmark: all estimators (exact, local_mc, smooth, neighborhood, variance, step, Stein) × τ ∈ {0.5, 2, 8, 16}/255 × 4 model subsets, for slope and control MSE.
  - Source: `CR/figures/nonlinear_control/biological_validation/site_centered_predictor_benchmark_control_session_pearson_fdr.png` (28 predictors) ✅
  - Or the `_export_pearson_10v9v8v7` version (16 predictors) ✅
- **Fig. S11 🆕** basic trace figures for **all 10 models**: s_k spectrum, q_k = ‖J^T v_k‖², q_k / s_k, cumulative T(κ) over PC index. One color per model, at matched df₂ or at each model's CV κ.
  - Only 4 models exist so far: `{robust_resnet50,standard_resnet50,clipag,dinov2}_seed10/pc_geometry.*`.
  - Data for all 84 geometries: `$STORE_DIR/.../nonlinear_control/mass_v1/geometry/*/summary.npz` (`exact_by_seed`, `spectrum`).
  - Needs a new plotting script (GPU not needed).
  - Interim option: `scale_energy/model_exact_energy_bars.*` ✅, showing Σq, T at df₂ = 375 and Σq/s for all 10 models.
- **Fig. S12** smoothing scale: site-centered correlation vs τ for each estimator family.
  - Source: `site_centered_{smooth,neighborhood}_correlations.png` ✅, or `synopsis_smoothing_level_correlations_control_session.png` ✅
  - Also `forward_noise/noise_geometry.*`: smoothed / exact T vs τ, 4 models ✅
- **Fig. S13** robustness (pick 2–3):
  - Residualization variants (`_subset_residualized` vs `_all10_reference_residualized`) ✅
  - Raw-x `paper_v4_raw_x` / `paper_v5_raw_predictors` ✅
  - Session endpoint bootstrap (`session_endpoint_image_bootstrap.png`) ✅
  - Encoding-session endpoint (`site_centered_predictor_benchmark_encoding_session.png`) ✅
- Estimator validation figures (could instead go in Methods B.6): `stein_stability_diagnostics.png`, `stein_nested_full_validation.png` ✅

---

## B. Detailed methods (empirical)

### B.1 Natural-image data and covariance ✍️
- van Hateren patches: 100×100, log(1+L)/log 65536, 8-bit quantization; 2k training pool and 20k population pool; empirical Σ and eigendecomposition. Most of this is already in `appendix_vanhateren_landscape_methods.tex` (currently App. K), so move it here.
- Disk teacher: radius 0.3, S = 1736.34.
- Mention the 16×16 and 32×32 variants only if the small-d validation figures are used.
- Drop FFHQ unless it is cited.

### B.2 Toy linear example (Fig. 1 bottom) ✍️
- Students: w₁ = w*; w₂ = w* + perturbation along low-variance PCs.
- Also needed: seed image, target levels r*, the α schedule (variance matching), and how the peer-review panels are computed.
- ⚠️ The script or notebook for `Figure_LinearToyModel` was **not found** in `CR/`. Need its location or its parameters.

### B.3 Two-PC geometry illustration (Fig. 2, Fig. S1) ✍️
- Σ = diag(1, ε = 0.04), λ = 0.05, σ² = 0.5, λ grid.
- Exact conditional Gaussian of β̂ | X; how the iso-sets are drawn.
- Source: `CR/notebooks/ridge_paths_geometry_explorer.ipynb`, `tables/ridge_paths_iso_error_geometry.csv`.

### B.4 Pixel-ridge landscape computation (Fig. 3) ✅
- Move the current `appendix_vanhateren_landscape_methods.tex` here unchanged: grid, DE evaluation, 100 paired MC trials, affine-in-σ caching, exact LOOCV.
- Small ✍️ addition: how the Fig. S4 curves were computed (Gaussian surrogate with 8,192 draws; E_acc oracle).

### B.5 Linear feature ridge: feature construction and rotation (Fig. 4, S6–S8) ✍️
- Top-p PC projector as the base feature map (p = 500 main, 100 alt), n = 1000.
- Tail loading t = sin²θ via rowwise Givens rotations high-PC → tail-PC in whitened coordinates. Point to theory G.3 for why this is prediction-null.
- Random null family: 300 randomized rowwise rotations and pairings.
- Noise levels σ²/S ∈ {0.01, 0.1, 1, 10}.
- DE-selected α vs empirical-CV α; number of MC trials; how T_F is computed.
- Sources: `CR/notebooks/README_top_pc_rotation.md`, `top_pc_rotation_experiment.ipynb`, `tables/vanhateren_top500_*`, `vanhateren_null_*`.

### B.6 Neural data (Prince, Wang et al. 2026) ✍️
- **Subjects and sites:** 5 monkeys × 5 sites.
  - red aIT, paul cIT, venus 3×V3 + 2×V4, leap STS, three0 STS.
  - ⚠️ The main text says "V2–IT"; check.
- **Encoding session:** 969 natural images (774 train / 195 held out); one split shared across rows.
- **Control session:**
  - 10 seed images; up to 11 target levels; 36–110 accentuated stimuli per site–model pair (median 102).
  - Re-presented held-out natural anchors: 50/50/50/24/22.
  - AnchorDay z-normalization; Leap duplicate merging.
- **Preprocessing:** upstream `pnc` repo at SHA 9b6fd95. Peak windows, outlier rejection, firing floor.
- **Cross-session affine calibration:**
  - Fit per site on encoding-train anchors, then freeze it and share it across models.
  - Evaluate on held-out anchors (E_val) and on accentuated images (control).
- **Endpoints:**
  - Control slope: OLS of measured on predicted over the accentuated cloud.
  - Control MSE: no refit.
  - E_val: held-out anchor MSE.

### B.7 Encoding models 🆕 table + ✍️
- Table: 10 models × (architecture, training objective, layers used across sites, # unique geometries).
  - Models: AlexNet (untrained?), RN50, robust RN50, CLIP-RN50, DINO-RN50, RegNetY-640, CLIPAG ViT-B/32, DINOv2 ViT-B/14-reg, SigLIP2 ViT-B/16, RADIO v2.5-B.
- **Feature pipeline:** layer activation → PCA750 fit on 774 train images → RidgeCV (α ∈ [1e-3, 1e6]); layer chosen per site by CV.
  - ⚠️ The main text omits the PCA750 step.
- ⚠️ Missing information: the AlexNet "untrained" checkpoint (`AlexNet_training_seed_01`) and the robust RN50 attack type / ε.

### B.8 Nonlinear diagnostic computation (Fig. 5) ✍️
- **κ from the CV α:** s_k is the PCA-score variance on train; solve κ(1 − df₁/n) = α/n with n = 774. Median κ ≈ 3.5, median df₂ ≈ 231.
- **Exact VJPs:**
  - One backward pass per PC (750), batched 32 at a time.
  - Taken on the 224×224 RGB grid (d = 150,528) in [0,1] units; normalization std divided out; resize not differentiated.
  - Averaged over the 10 seeds.
- **Neighborhood estimators:**
  - τ ∈ {0.5, 2, 8, 16}/255, R = 64 directions, L = 8 centers.
  - smooth: debiased U-statistic. neighborhood, variance (jackknife drift removal), step.
  - local_mc: finite-difference h check.
  - Antithetic Stein: R = 512.
- Put the formulas in theory App. I; put the numbers here.
- Validation checks: 84/84 geometries; residual ≤ 6e-8; ~1.4 H100-hours.

### B.9 Statistical analysis ✍️
- Site-centering of log predictors and of outcomes; Pearson, Spearman, cluster-robust OLS.
- Model subsets 10/9/8/7.
- BH-FDR within endpoint × subset.
- Image bootstrap: 2,000 resamples. Leave-one-monkey-out and leave-one-model-out regressions.
- Caveat: models are nested within sites (repeated measures).

### B.10 Neural peer-review analysis ✍️
- Build the 25 × 10 × 10 site–generator–reviewer cells with the same frozen affine map.
- Metrics: MSE, r, identity R², slope. Aggregation: equal-weight mean over sites.
- Self (diagonal) vs peer (off-diagonal) tests:
  - Reviewer-label permutation (200k).
  - Wilcoxon over generators.
  - Subject sign-flip.
  - Subject bootstrap (100k).

### B.11 Software and compute ✍️ (short)

---

## Consistency issues found while planning (fix in the main text)
1. **Sec. 2 "better calibration than the generator":** the peer-review analysis finds |slope − 1| similar or *larger* for peer than for self. The slope is > 1 (under-prediction), not calibrated. Rephrase to "correct sign / bounded error" rather than "better calibration".
2. **Sec. 6 numbers vs Fig. 5 caption vs latest tables:**
   - Text: exact-local V_φ r = 0.62 (slope) and 0.44 (MSE) with 9 models; conventional-7 about 0.2; held-out MSE 0.03 / −0.07.
   - Caption: Neighborhood-16 r = −0.56, 250 pairs.
   - Latest export (`SCALE_ENERGY` / v1.4 synopsis): Neighborhood-16 r = −0.614 / −0.605 / −0.300 / −0.191 for 10 / 9 / 8 / 7 models. Exact T gives 0.541 with 10 models but only 0.009 with 8.
   - Pick one source table (control-session endpoint, v1.4) and regenerate every quoted number from it.
   - Theory App. I.1 repeats the same (older) numbers.
3. **The exact T signal disappears without the robust models** (8-subset r ≈ 0.01), while neighborhood / variance at 16/255 keeps about 0.3. The Sec. 6 sentence "the trace T_φ alone does nearly as well" needs qualifying. This argues for featuring the neighborhood estimator.
4. **Main-text footnote** says App. treats nonzero / multiple seeds, but App. C.3 says "we do not pursue these". Either port `CR/notes/accentuation_nonzero_multiseed_theory.tex` or reword the footnote.
5. **Undefined refs:** `suppfig:pixl-MC` (→ Fig. S2), an empty `\ref{}` in the Fig. 3 caption (→ Fig. S2), `eq:app`, `close_condition`.
   **Undefined cites:** `?`, `XXX`, `alex`, `blake`, `surya`.
6. **Sec. 2** says ridge with "penalty and layer chosen by CV" on network features; it should mention the PCA750 step and the per-site layer choice.
7. **Duplication:** theory App. I.1 (empirical validation) overlaps Sec. 6. After B.8 and A.5 exist, trim I.1 to one pointer paragraph.

8. **Sec. 2 "V2--IT"**: the actual areas are V3/V4 (venus), cIT (paul), aIT (red) and STS (leap, three0). Also, "~1000 natural images" is really 969 images: 649 NSD shared1000 + 259 segmented objects/animals + 61 fLoc. They are not all natural images.
9. **Sec. 2 "penalty and layer chosen by cross-validation"**: the penalty comes from RidgeCV (efficient LOO; α grid 1e-4 to 1e9, one α per channel). The layer was chosen per channel by R² **on the 195-image held-out split**, the same split that later reports encoding accuracy. Selection and reporting share data, so this should be stated in B.7.
10. **Data source**: the data are **not** from BrainScore. They come from lab storage / Zenodo (the record is not yet minted). BrainScore only hosts the untrained AlexNet weights.
11. **`AlexNet_training_seed_01` really is a random initialization** (verified from the weight distribution). The upstream `L/README.md` calls it a "Custom trained variant", which is misleading. The main-text "untrained AlexNet" is correct.
12. **Checkpoint sources are undocumented** for the robust RN50 (`imagenet_linf_8_pure.pt`, probably from Madry-lab robustness / Salman 2020) and for CLIPAG (`CLIPAG_ViTB32.pt`, Ganz & Elad 2023). Both need confirming for the citations.
13. **Upstream inconsistency**: `resnet50_clip` used ImageNet normalization at synthesis but the CLIP transform at fitting. Consider a footnote.
14. **The cross-session affine calibration is our downstream analysis choice**, not upstream (upstream uses anchorDay z-scoring only). B.6 should say so explicitly, together with the difference from the upstream metrics (control_r, control_slope, identity control_R2; there is no MSE upstream).
15. **Citations to add**: Prince, Wang et al. bioRxiv 10.64898/2026.08.16.745063; NSD (Allen 2022); fLoc (Stigliani 2015); MACO (Fel 2023); Horama; each backbone paper (see the B.7 table).

16. **Fig. 1 toy setup vs main-text wording**:
    - The two students are *constructed* (w* + a low-variance eigen-direction), not fitted by regression.
    - Accentuation starts from natural seeds (closed form), not from the null seed.
    - The van Hateren preprocessing (min-max normalization, −0.15 offset) differs from the Fig. 3 pipeline (log luminance).
    - The Fig. 1C R² values (0.9969 / 0.0481) do not match the script's cross-eval figure (0.9966 / −9.94), so they probably use a different denominator. Unify these with the paper's R² definition.

## Open questions for Binxu (answered above, 2026-09-24)
- Q1. Order: Extended results → Methods → Theory (current plan), or Methods → Extended results → Theory?
- Q2. Should the dependency graph and null-rotation figures move from theory G into A.3, or stay in G with A.3 pointing to them?
- Q3. Where is the code for the Fig. 1 bottom toy model (and the geometry inset)?
- Q4. Which checkpoint is the "untrained AlexNet", and what are the robust RN50 training details (attack, ε)?
- Q5. Fig. S11 (per-model spectra): matched df₂ (= 375) or each site's CV κ? One panel per model, or overlaid?
- Q6. Include the synthetic (isotropic / power-law) validation (Fig. S5) or keep the appendix natural-image only?
