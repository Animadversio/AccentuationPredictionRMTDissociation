# Page trim v3: equation/proposition layout + remaining text (2026-09-26)

Measured on the current `main_body_compact.tex`, which ends at line 486 (1 line into p.10). p.9 holds lines 432–485. Every number below comes from an actual build.

| Tier | What | Main text ends at | Spare lines |
|---|---|---|---|
| now | none | 486 | −1 |
| 1 | §6 + Fig. 5 + Limitations (4 paragraphs) | 478 | 7 |
| **2 (recommended)** | Tier 1 + equation/prop layout + peer review | **472** | **13** |
| 3 | Tier 2 + the optional front/§5 edits | 460 | 25 |

`main_body_compact_trimmed.tex` currently holds **Tier 2** (driver: `accentuation_rmt_main_compact_trimmed.tex`).

Tightening the theorem-environment spacing (`\newtheoremstyle` with 4pt) saved **0 lines**, so it is not proposed.

**Panel references to check (unrelated to length).** The new composite Fig. 1 has panels A (experiment), B.I–III (neurons), C (linear) and D (geometry). The text still says "Fig. 1, top", "top right", "Fig. 1A" (matched prediction, now B.I?) and "Fig. 1B,C" / "Fig. 1C" (peer review, now B.III?). §3 also says "Fig. 1 (bottom)".

## Tier 1: required (§6)

### §6, Fig. 5 caption (from "We reproduced the results…" to the end of the caption)  ·  T28

9 lines become about 6.

```latex
Published preprocessed data of \citetPW.
\textbf{A}~Held-out natural-image MSE in the control session ($E_{\mathrm{val}}\approx E_{\mathrm{gen}}+\sigma^2$).
\textbf{B}~Slope of measured on predicted responses to accentuated stimuli. \textbf{A,B}: mean over 25 sites (bars), sites (dots), $\pm1$ SE.
\textbf{C}~Raw $\log_{10}V_\phi$ ($16/255$ neighborhood) against control slope with each site's ten-model mean removed (Pearson $r=-0.56$, 250 site--model pairs).
\textbf{D}~Pearson $-r$ between site-centered control slope and seven raw $\log_{10}$ predictors (held-out MSE, $T_\phi(\kappa)$, exact-local and neighborhood $V_\phi$ at four scales) for 10/9/8/7-model subsets (all / no untrained AlexNet / no robust models / neither); stars: raw two-sided $p<0.05$. All estimators: App.~\ref{sec:app-ext-nonlinear}.} %without multiple-comparison correction
```

### §6 first paragraph, the last two sentences (from "For linear $\phi$ this is exact…")  ·  T29

Condensed.

```latex
It is exact for linear $\phi$ and a theory-motivated diagnostic for networks, where $s_k=g_k^\top\Sigma g_k$ no longer holds. Since an accentuation path travels far from the seed, we also average the Jacobian, or the squared gradient, over a Gaussian neighborhood of the seed at pixel-noise scales $0.5$--$16/255$ (App.~\ref{sec:app-nonlinear-diagnostic}).
```

### §6 results paragraph, the ending  ·  T30

Delete the final caveat sentence ("These are descriptive associations … would also be needed."); it moves to Limitations.

```latex
… by far the smallest $T_\phi$. Neighborhood-smoothed versions preserve or slightly improve the ordering.
```

### §7 Limitations  ·  T32

Takes the §6 caveats.

```latex
\paragraph{Limitations.}
The theory assumes Gaussian inputs, a linear teacher, a fixed linear feature map and a one-dimensional accentuation path from a centered seed; the leading DEs predict typical fits and the location of the control optimum but not the fluctuation-dominated error at that optimum (App.~\ref{sec:app-ratio-corrections}). The nonlinear diagnostic is not a theorem; its biological validation is descriptive (repeated models within sites) and concerns model ordering, not absolute control error. Extending the DEs to learned nonlinear features and curved accentuation paths is the natural next step.
```

## Tier 2: equation / proposition layout and peer review

### Toolkit: replace the sentence "Results use the teacher-weighted…" plus the unlabeled $B_{p,q}$ display  ·  E5

The unlabeled display becomes inline (about 2 lines).

```latex
Results use the teacher-weighted and unweighted spectral sums $B_{p,q}(\kappa)=\sum_ks_k^pb_k^2/(s_k+\kappa)^q$ and $\mathrm{df}_{p,q}(\kappa)=\sum_ks_k^p/(s_k+\kappa)^q$ ($\mathrm{df}_2:=\mathrm{df}_{2,2}$), so that, for instance, $\bstar^\top\bar\beta_\kappa=B_{1,1}$ and $\|\bar\beta_\kappa\|^2=B_{2,2}$. 
For the ratio $N/D$ we use the leading approximation $\mu_N/\mu_D$ from the DEs of $N$ and $D$; second-order and distributional refinements matter only where the leading calibration error is already small (App.~\ref{sec:app-ratio-corrections}).
```

### Prop. 1, the lead sentence (and delete the standalone "(Proofs and the per-mode decomposition…)" line before \end{prop})  ·  E1

The proof pointer moves into the lead.

```latex
With $\kappa$, $B$ and $\mathrm{df}$ built from $\Sigma$ (proofs and per-mode decomposition: App.~\ref{sec:app-pixel-ridge}),
```

### Prop. 2, the whole statement (from "Among admissible values…" to \end{prop})  ·  E2

Shorter lead with the proof pointer; $z^{(0)}_{acc,CV}$ becomes the third row of the same `align` (all three labels kept). The "Further, at the prediction optimum…" line and the separate display are gone. **!** "Among admissible values of κ" is dropped (it is kept in the appendix statement).

```latex
Let $\kappa_{\rm gen}^{\star}$ be an interior differentiable minimizer of $E_{\rm gen,DE}$ and $\kappa_{\rm acc}^{\star}$ a zero of the leading control error, $\mu_D=\mu_N$ (proofs: App.~\ref{sec:app-optimal-regularization}). Then
\begin{align}
E_{\rm gen,DE}+\sigma^2
&=n\kappa\frac{B_{2,3}}{\mathrm{df}_{2,3}},
&&(\kappa=\kappa_{\rm gen}^{\star};\ \text{prediction stationarity}),
\label{eq:gen_optim_reg_cond}\\
E_{\rm gen,DE}+\sigma^2
&=n\kappa\frac{B_{1,2}}{\mathrm{df}_{1,2}},
&&(\kappa=\kappa_{\rm acc}^{\star};\ \text{zero leading control error}),
\label{eq:acc_optim_reg_cond1}\\
z^{(0)}_{acc,CV}
&=\frac{\kappa\,\mathrm{df}_{1,2}}{B_{1,1}}\Big(\frac{B_{2,3}}{\mathrm{df}_{2,3}}-\frac{B_{1,2}}{\mathrm{df}_{1,2}}\Big),
&&(\text{control error at }\kappa=\kappa_{\rm gen}^{\star}).
\label{eq:pixel-zacc-cv}
\end{align}
\end{prop}
```

### Prop. 3, the lead and the two displays (the "Then" between them goes)  ·  E3

One `gather` with both labels; restores `\quad` spacing between the three definitions.

```latex
With $\kappa$, $B^F$ and $\mathrm{df}^F$ built from $(\Sigma_F,w^\star)$ and aspect ratio $p/n$, the mean pixel weight is the realizable weight shrunk in feature space and back-projected, and the norm inflation carries a \emph{gradient-geometry factor} $T_F$:
\begin{gather}
\bar\beta_{F,\kappa}:=F^\top(\Sigma_F+\kappa I)^{-1}F\Sigma\bstar,\quad V_F(\kappa):=\frac{E_{gen,DE}+\sigma^2}{n}\,T_F(\kappa),\quad T_F(\kappa):=\operatorname{Tr}\big[\Gram(\Sigma_F+\kappa I)^{-2}\Sigma_F\big],
\label{eq:feature-mean-variance}\\
E_{gen,DE}=\frac{n(\kappa^2B^F_{1,2}+S_\perp+\sigma^2)}{n-\mathrm{df}^F_2}-\sigma^2,\qquad N_{DE}={\bstar}^\top\bar\beta_{F,\kappa},\qquad D_{DE}=\|\bar\beta_{F,\kappa}\|^2+V_F(\kappa).
\label{eq:feature-de}
\end{gather}
```

### Prop. 4 statement  ·  E4

"hence the joint feature–response covariance, $E_{gen,DE}(\kappa)$ and the DE-based prediction-optimal penalty" becomes "hence $E_{gen,DE}(\kappa)$ and $\kappa^\star_{gen}$".

```latex
\begin{prop}[Prediction-preserving gauge]\label{prop:gauge}
For $\Sigma\succ0$ and any orthogonal $Q$ with $Q\Sigma^{1/2}\bstar=\Sigma^{1/2}\bstar$, the map $F\mapsto F\Sigma^{1/2}Q\Sigma^{-1/2}$ preserves $\Sigma_F$ and $F\Sigma\bstar$, hence $E_{gen,DE}(\kappa)$ and $\kappa^\star_{gen}$, while changing $\Gram$ and $F\bstar$ and therefore control (Prop.~\ref{prop:mr-gauge}; construction in App.~\ref{sec:app-gauge-fragility}).
\end{prop}
```

### Peer review, from "The sign differences in neural data…" to the end of the paragraph  ·  T23, T24

The neural stats become one clean sentence (same numbers); the symmetry note goes from 3 lines to 1. **!** It drops the "recognize its own noise" mechanism, which stays in App. J.5.

```latex
The neuronal data of \citetPW\ show the same signs: peer review gives $R^2=0.04$ $[-0.06,0.10]$ and slope $1.35$ $[1.14,1.59]$ (median [IQR], $n=90$ model pairs), self-accentuation $R^2=-4.17$ $[-4.59,-3.51]$ and slope $0.38$ $[0.33,0.42]$ ($n=10$; Apps.~\ref{sec:app-ext-peer},~\ref{sec:app-methods-peer}). % stats test between the two \todo
This pixel-space peer review is symmetric between the two fits; students fitted to the same recordings through different feature maps review each other asymmetrically (App.~\ref{sec:app-peer-shared}).
```

### Fig. 4 caption, the final pointer  ·  T25

```latex
Construction and more rotations: Apps.~\ref{sec:app-methods-feature},~\ref{sec:app-ext-gauge}.}
```

## Tier 3: optional (front matter, §5, Discussion)

### §2 opening paragraph ("\citetPW used the following closed-loop paradigm…")  ·  X4

Tightened; fixes "a image"; the pointer is now Fig. 1A to match the new composite (see the panel note below).

```latex
\citetPW\ used a closed-loop paradigm (Fig.~\ref{fig:phenomena}A): responses of visual cortical sites (V2--IT, 25 sites in 5 macaques) to $\sim$1000 natural images were recorded; for each site, ten encoding models were fit by ridge regression on features of ten deep-network backbones, with penalty and layer chosen by cross-validation; each model then used gradient-based \emph{feature accentuation} \citep{hamblin2024feature} to synthesize images driving its own prediction to eleven target levels from ten seed images, which were presented to the same sites in a \textit{control session}. Control succeeds if the images evoke the predicted responses (Apps.~\ref{sec:app-methods-neural-data},~\ref{sec:app-methods-models}). Three observations motivate this paper.
```

### Abstract, first two sentences  ·  T1

Merged; grammar fixed.

```latex
Recent experiments show that models with similar held-out accuracy in predicting visual-neuron responses can differ sharply in their ability to generate stimuli that control those neurons, and that control success tracks the structure of a model's input gradient more than its predictive accuracy.
```

### Abstract, last sentence  ·  T2

```latex
The resulting gradient-geometry factor extends to nonlinear networks as a diagnostic that orders models' \textit{in vivo} control better than held-out accuracy.
```

### Contributions (ii) and the closing sentence  ·  T3, T4

Fixes "we also restates" and removes the "section." short trailing line.

```latex
\textbf{(ii)} deterministic equivalents for pixel-space ridge regression showing that prediction-optimal and control-optimal penalties satisfy different spectral conditions, so cross-validation leaves a computable residual control error under anisotropic data (Sec.~\ref{sec:pixel});
…
All results are proved in the appendix, which restates them in derivation order (App.~\ref{sec:app-main-results}), and each is validated by Monte Carlo and natural-image regression.
```

### §3 "Teacher and student", last sentence  ·  T9

```latex
The student is $f(\x)=\x^\top\bhat$, fitted from $n$ pairs $(X,\mathbf y)$; for a linear feature-space student (Sec.~\ref{sec:feature}) $\bhat=F^\top\hat w$ is the effective pixel weight, i.e.\ $\nabla_\x f$.
```

### Fig. 2 (wrapfig) caption  ·  T11

Shorter; also fixes #22/#23 ("prediction-optimal penalty", "noise-averaged path").

```latex
\caption{\textbf{Equal-error sets and the ridge path} in the plane of a high- and a low-variance PC: prediction ellipsoids around $\bstar$ (blue), control spheres on the diameter $[0,(1+z)\bstar]$ (orange). One fitted weight moves through the plane as $\lambda$ varies (purple), around its noise-averaged path (dashed). The prediction-optimal penalty is the path's tangency with an ellipsoid; perfect control is its crossing of the $z=0$ sphere. Construction: App.~\ref{sec:app-ext-geometry}.}
```

### §5 summary box, last sentence  ·  T27

```latex
Noisy neuronal responses \red{\cite{?}} supply (i), natural images make (ii) large for every model, and the feature map decides (iii), in which equally predictive maps can differ without bound.
```

### §5 sentence before Prop. 4 and the sentence after it  ·  N4, T26

```latex
This extra freedom is exposed by the group of map transformations that leave prediction unchanged.
…
The gauge changes control only for anisotropic inputs, increasingly so with anisotropy.
```

### §7 Discussion  ·  T31

```latex
A single mechanism accounts for the three neuronal phenomena: prediction measures weight error in the covariance metric, control along the model's own gradient. At fixed prediction error, control error is governed by noise, spectrum and map (Sec.~\ref{sec:feature}), and only the first is visible in held-out accuracy. Selecting encoding models or penalties by held-out prediction therefore cannot certify gradient-based control; validation must constrain the gradient, e.g.\ through $T_\phi$, or test generated stimuli directly. High-frequency artifacts of failed accentuations are the expected signature of low-variance directions that natural images never constrained.
```
