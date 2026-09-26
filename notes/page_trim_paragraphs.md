# Page trim, paragraph by paragraph (v2, 2026-09-26)

Based on the **current** `main_body_compact.tex` (after your merge). With all 17 replacements below, the main text ends at **line 478 of p.9**, which holds lines 432–485, so 7 lines are to spare. Your current file ends at line 499, about 15 lines into p.10.

The same text is already assembled in `main_body_compact_trimmed.tex` (driver: `accentuation_rmt_main_compact_trimmed.tex`), so you can compare on Overleaf.

**Which ones are needed.** These were measured with one build per combination:
- **§4 group (T12–T22) and §6 group (T28–T32): required.** Dropping either leaves the text on p.10.
- **§5 group (N1, N2, N4, T26, T27): buffer.** Without it the text still fits, ending at line 483 with only 2 lines to spare.
- **Abstract, intro, Fig. 1, §3 and peer-review edits from v1 (T1–T11, T23–T25): not needed** for the limit. Keep them only if you like the wording.

All numbers are unchanged. Each item gives the **full new paragraph** to paste over the old one.

## 1. §4 opening, the sentence after Eq. (ridge)  ·  T12

Two sentences become one.

```latex
Ridge penalizes weight in low-variance directions, so one might expect it to remove these control-vulnerable components; we ask whether they survive a cross-validated penalty.
```

## 2. §4 ¶ "The ridge path through the two landscapes"  ·  T13

The last sentence is merged into the previous one.

```latex
\paragraph{The ridge path through the two landscapes.}
The question has a geometric reading (Fig.~\ref{fig:geometry}). For a given training set, Eq.~\ref{eq:ridge} traces a path $\bhat(\lambda)$ in weight space from the least-squares or minimum-norm solution at $\lambda\to0$ to the origin at $\lambda\to\infty$. Response noise and the random design scatter the fitted weight in a cloud around its mean. Ideally, cross-validation selects the point where the path is tangent to the smallest reachable prediction ellipsoid; whereas minimal control error asks where the path crosses the $z=0$ sphere $D=N$; in general the two points differ, and the analysis below makes this quantitative. 
%\red{the two coincide only if the noise cloud has not pushed the path off the sphere in the directions the ellipsoid does not see. The deterministic equivalents below compute where the center of this cloud sits, how much Euclidean spread it carries, and hence the distance between the two points.}, and the cloud is elongated along the low-variance directions of $\Sigma$, because those are the directions the data constrain least
```

## 3. §4 ¶ "Toolkit", up to the $B_{p,q}$ display  ·  T14, T15

κ definition compacted; the redundant "DE allows us…" sentence was dropped; the norm-inflation sentences merged. **Largest single saving.**

```latex
\paragraph{Toolkit.}
We use deterministic equivalents (DEs) in the proportional limit $d/n\to\gamma$ \citep{dobriban2018high,hastie2022surprises}. They replace functions of the empirical covariance $\hat\Sigma$ by deterministic functions of the population covariance $\Sigma$, e.g. $\hat\Sigma(\hat\Sigma+\lambda I)^{-1}\asymp\Sigma(\Sigma+\kappa I)^{-1}$, where the finite-sample randomness is absorbed into an effective penalty $\kappa(\lambda)\ge\lambda$, the unique positive root of $\kappa-\lambda=\frac{\kappa}{n}\operatorname{Tr}[\Sigma(\Sigma+\kappa I)^{-1}]$, one-to-one in $\lambda$ (App.~\ref{sec:app-de-toolkit}).
Applied to Eq.~\ref{eq:ridge}, the DE says that the signal term concentrates around a \emph{mean fitted weight}, the teacher shrunk mode by mode,
\begin{equation}
\bar\beta_\kappa:=\Sigma(\Sigma+\kappa I)^{-1}\bstar=\sum_k\frac{s_k}{s_k+\kappa}\,b_k\uvec_k ,
\label{eq:pixel-mean-weight}
\end{equation}
while the noise term has zero mean but carries Euclidean energy, the \emph{norm inflation} $V:=\E\|\bhat\|^2-\|\bar\beta\|^2\ge0$, which drives accentuation error. The mean weight $\bar\beta$ and inflation $V$ also organize the feature-space case and the nonlinear diagnostic (Secs.~\ref{sec:feature},~\ref{sec:nonlinear}). Results use the teacher-weighted and unweighted spectral sums
```

## 4. Fig. 3 caption, the A–C part  ·  T16

A–C condensed; the MC-validation sentence became a parenthesis.

```latex
\textbf{A--C}~DE landscapes (Eq.~\ref{eq:pixel-de}) of $E_{gen}$, $E_{acc}$ and $R^2_{acc}$ over noise $\sigma^2/S$ and effective penalty $\kappa$ (Monte Carlo: Fig.~\ref{fig:supp-pixel-de-mc}). The prediction-optimal and median empirical RidgeCV paths track each other but not the control-optimal path; black contour: $R^2_{acc}=0$.
```

## 5. §4 reading of Prop. 1 ("$E_{gen}$ recovers…")  ·  T17, T18

Dropped "The two control moments have a plain reading" and "The second term of D is the key issue".

```latex
$E_{gen}$ recovers the classical in-distribution generalization error \citep{dobriban2018high,hastie2022surprises}. $N$ is the alignment of the teacher with the mean fitted weight, and the first term of $D$ is that weight's squared norm; both are set by the teacher and the shrinkage alone, and since each factor $s_k/(s_k+\kappa)$ lies in $[0,1]$ they are ordered $\|\bstar\|^2\ge B_{1,1}\ge B_{2,2}$ (Eq.~\ref{eq:app-spectral-inequalities}), so the mean weight by itself \emph{under}-shoots its own path ($D<N$, slope above one). The second term, $V_{\rm pix}$, is how limited data $n$, response noise $\sigma^2$ and prediction error $E_{gen}$ jointly inflate the student norm, amplified by the spectral susceptibility $\mathrm{df}_{1,2}=\sum_ks_k/(s_k+\kappa)^2$, which counts the modes near the threshold $\kappa$.
```

## 6. §4 after Prop. 2, the last two sentences of the kernel paragraph  ·  T20

Tightened; ends "(slope_acc < 1)".

```latex
For \textit{an anisotropic spectrum and a structured teacher} the averages differ, and their difference is the control error left at the cross-validated penalty. When $b_k^2$ decreases toward the low-variance tail, as for a teacher aligned with high-variance image modes, $z^{(0)}_{acc,CV}>0$ and the cross-validated student over-predicts ($\mathrm{slope}_{acc}<1$).
```

## 7. §4 landscape paragraph ("We visualize the landscape…")  ·  T21

4 sentences become 3; no content lost.

```latex
Over the noise--regularization plane for natural images (Fig.~\ref{fig:pixel}A--C), the DE tracks Monte Carlo except at very low noise or regularization (Fig.~\ref{fig:supp-pixel-de-mc}). Prediction- and control-optimal penalties form two distinct valleys, the $E_{acc}$ valley a sharp cusp. At low noise $\kappa^\star_{\rm gen}$ is also benign to control; as noise grows it approaches and crosses the $R^2_{acc}=0$ cliff, and control fails catastrophically.
```

## 8. §4 closing sentence ("This answers the question in the title…")  ·  T22

Condensed.

```latex
For pixel regression, then, \emph{control is bad despite prediction-optimal regularization when the response is noisy, the spectrum anisotropic and many modes sit near $\kappa$}: the regime of noisy neurons viewing natural images.
```

## 9. Fig. 4 float specifier  ·  N1

`\begin{figure}[!htp]` becomes `\begin{figure}[t]`, avoiding mid-page float gaps.

```latex
\begin{figure}[t]
```

## 10. Prop. 3 displays  ·  N2

Two displays plus "Then" become one `gather` with both labels. Also restores `,\quad` spacing: the current `\,` makes the three definitions run together.

```latex
\begin{gather}
\bar\beta_{F,\kappa}:=F^\top(\Sigma_F+\kappa I)^{-1}F\Sigma\bstar,\quad
V_F(\kappa):=\frac{E_{gen,DE}+\sigma^2}{n}\,T_F(\kappa),\quad
T_F(\kappa):=\operatorname{Tr}\big[\Gram(\Sigma_F+\kappa I)^{-2}\Sigma_F\big],
\label{eq:feature-mean-variance}\\
E_{gen,DE}=\frac{n(\kappa^2B^F_{1,2}+S_\perp+\sigma^2)}{n-\mathrm{df}^F_2}-\sigma^2,\qquad
N_{DE}={\bstar}^\top\bar\beta_{F,\kappa},\qquad
D_{DE}=\|\bar\beta_{F,\kappa}\|^2+V_F(\kappa).
\label{eq:feature-de}
\end{gather}
```

## 11. §5 sentence before Prop. 4  ·  N4

Removes the short trailing line "without affecting prediction.".

```latex
This extra freedom is exposed by the group of map transformations that leave prediction unchanged.
```

## 12. §5 sentence after Prop. 4  ·  T26

The two white-data remarks merged.

```latex
The gauge changes control only for anisotropic inputs, increasingly so with anisotropy.
```

## 13. §5 Summary box, last sentence  ·  T27

One sentence; the `\cite{?}` is kept.

```latex
Noisy neuronal responses \red{\cite{?}} supply (i), natural images make (ii) large for every model, and the feature map decides (iii), in which equally predictive maps can differ without bound.
```

## 14. Fig. 5 caption  ·  T28

9 lines become about 6.

```latex
Published preprocessed data of \citetPW.
\textbf{A}~Held-out natural-image MSE in the control session ($E_{\mathrm{val}}\approx E_{\mathrm{gen}}+\sigma^2$).
\textbf{B}~Slope of measured on predicted responses to accentuated stimuli. \textbf{A,B}: mean over 25 sites (bars), sites (dots), $\pm1$ SE.
\textbf{C}~Raw $\log_{10}V_\phi$ ($16/255$ neighborhood) against control slope with each site's ten-model mean removed (Pearson $r=-0.56$, 250 site--model pairs).
\textbf{D}~Pearson $-r$ between site-centered control slope and seven raw $\log_{10}$ predictors (held-out MSE, $T_\phi(\kappa)$, exact-local and neighborhood $V_\phi$ at four scales) for 10/9/8/7-model subsets (all / no untrained AlexNet / no robust models / neither); stars: raw two-sided $p<0.05$. All estimators: App.~\ref{sec:app-ext-nonlinear}.} %without multiple-comparison correction
```

## 15. §6 first paragraph, the last two sentences  ·  T29

"Exact for linear φ; theory-motivated diagnostic for networks"; the smoothing sentence was shortened.

```latex
It is exact for linear $\phi$ and a theory-motivated diagnostic for networks, where $s_k=g_k^\top\Sigma g_k$ no longer holds. Since an accentuation path travels far from the seed, we also average the Jacobian, or the squared gradient, over a Gaussian neighborhood of the seed at pixel-noise scales $0.5$--$16/255$ (App.~\ref{sec:app-nonlinear-diagnostic}).
```

## 16. §6 results paragraph, the ending  ·  T30

The caveat sentence moved to Limitations (see T32); the rest of the paragraph is unchanged, numbers included.

```latex
…consistent with the two adversarially trained models being the strongest controllers and having by far the smallest $T_\phi$. Neighborhood-smoothed versions preserve or slightly improve the ordering.
```

## 17. §7 Limitations  ·  T32

Takes the §6 caveats; "DEs" instead of "deterministic equivalents".

```latex
\paragraph{Limitations.}
The theory assumes Gaussian inputs, a linear teacher, a fixed linear feature map and a one-dimensional accentuation path from a centered seed; the leading DEs predict typical fits and the location of the control optimum but not the fluctuation-dominated error at that optimum (App.~\ref{sec:app-ratio-corrections}). The nonlinear diagnostic is not a theorem; its biological validation is descriptive (repeated models within sites) and concerns model ordering, not absolute control error. Extending the DEs to learned nonlinear features and curved accentuation paths is the natural next step.
```
