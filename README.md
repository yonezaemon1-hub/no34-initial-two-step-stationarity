# No.34 — An Eight-Vertex Counterexample to Initial Two-Step Stationarity in Majority Dynamics

**Author:** Ryutaro Yonezu (Yonezu Research Lab)  
**Version/date:** 1.0 / 2026-10-23  
**Type:** Unrefereed research preprint  
**Rights:** All rights reserved (`LICENSE.txt`)  
**Scholarly novelty and priority:** Not established; this repository makes no priority claim  
**Contact:** yonezaemon1+research@gmail.com  
**Zenodo (v1.0):** [Published preprint](https://zenodo.org/records/23592417)  
**Version DOI:** [10.5281/zenodo.23592417](https://doi.org/10.5281/zenodo.23592417)

## Main result

In synchronous strict-neighbour-majority dynamics on a finite simple graph of odd degrees, there is an eight-vertex example with **no vertex** satisfying `s[t+2,v]=s[t,v]` for **all** `t>=0`. This is the exact negation of the all-time quantification in the *Stabilisation time* question in Section 6 of Benjamini, Zakharov and Zhukovskii, *Majority dynamics on finite trees*, arXiv:2507.04714 (2025); published in *Random Structures & Algorithms* (2026), DOI 10.1002/rsa.70092.

Crucial distinction: **0-stable** asks only about even times; **0-stationary** requires equality at both even and odd times. This result refutes the latter universal assertion. It does **not** refute existence of an even-time 0-stable vertex.

## Explicit witness

Vertices: `0..7`.

Edges: `01 03 05 12 13 15 16 23 24 34 35 46 67`.

Degrees in vertex order: `(3,5,3,5,3,3,3,1)`.

Initial spins: `+++---+-`.

| Time | Spins of vertices 0..7 |
|---:|:---|
|0|`+++---+-`|
|1|`-+-+++-+`|
|2|`+-++-++-`|
|3|`++-+++-+`|
|4|`++++-++-`|
|5|`++++++-+`|
|6|`+++++++-`|
|7|`++++++++`|
|8|`++++++++`|

First violation of `s[t+2,v]=s[t,v]` by vertex: `(1,0,3,0,4,0,5,6)`. The final all-positive state is fixed.

## Computer-assisted additional claims

- **Minimum vertex count 8**, within the all-odd-degree graph model (enumeration of all `n=2,4,6` examples and their initial states).
- **Minimum 13 edges among eight-vertex all-odd-degree graphs**, not necessarily globally across larger graphs.
- At `(n,m)=(8,13)`, **20,160 successful labelled graphs** form one graph-isomorphism class; on the displayed graph, the successful initial-state masks `71,102,153,184` are one class under graph automorphism and global sign reversal.

The 8-vertex enumeration considers `2^21 = 2,097,152` all-odd-degree labelled graphs. Two C++20 enumeration approaches agree in their recorded logs. An external adversarial examiner reported a separate full re-enumeration, but **did not** report running the bundled C++ files. This is not peer review. Claims of exhaustive minimality/classification remain explicitly computer-assisted.

## Files

- `No34_Preprint_v1_0.pdf` — 4-page research preprint.
- `No34_Preprint_v1_0.tex` — matching LaTeX source.
- `witness.json` — witness and trajectory certificate.
- `verify_witness.py`, `verify_parity_scope.py`, `verify_orbit.py` — direct checks.
- `verify_small_odd_degree_graphs.py` — complete enumeration at `n=2,4,6`.
- `verify_exhaustive_8_parity.cpp`, `verify_exhaustive_8_gray.cpp` — independently structured C++20 8-vertex enumeration implementations.
- `census_parity.log`, `census_gray.log` — recorded outputs of C++ enumerations.
- `AUDIT_STATUS.md` — explicit scope of verification and unresolved novelty.
- `LICENSE.txt`, `SHA256SUMS.txt` — rights and archive integrity.

## Reproduction

From the repository root (Python 3, C++20 compiler):

```sh
python verify_witness.py
python verify_parity_scope.py
python verify_orbit.py
python verify_small_odd_degree_graphs.py

# Comprehensive enumerations; may take substantial CPU time:
g++ -std=c++20 -O3 verify_exhaustive_8_parity.cpp -o no34_parity
./no34_parity
g++ -std=c++20 -O3 verify_exhaustive_8_gray.cpp -o no34_gray
./no34_gray
```

Compare the output of both programs with `census_parity.log` and `census_gray.log`. An SHA256 manifest is provided; this README itself is not included in the manifest to avoid a circular hash.

## Limitations and citation

The existence of the finite witness is directly checked. The exact minimality/classification claims require the provided exhaustive programs and inspection of their outputs. The prior-art survey is incomplete. **No scholarly priority, comprehensive novelty, or formal peer-review claim is made.** Do not cite this as a refereed paper.

Reference: Ryutaro Yonezu (2026), *An Eight-Vertex Counterexample to Initial Two-Step Stationarity in Majority Dynamics*, preprint v1.0, 23 October 2026. DOI: [10.5281/zenodo.23592417](https://doi.org/10.5281/zenodo.23592417).

Research inquiries: yonezaemon1+research@gmail.com
