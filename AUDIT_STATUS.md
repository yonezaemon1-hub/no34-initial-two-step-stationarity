# No.34 v1.0 — Verification record and limits

Date: 2026-10-23. Prepared from the separately archived internal v0.4 dossier.

| Category | Current status | Specific scope |
|---|---|---|
| Finite witness | PASS | Degree sequence, update trace, first violating times; re-executed independently of the paper text |
| Parity | PASS | 0-stable vertices `{0,2,6}` and 1-stable vertices `{1,3,4,5,7}` are disjoint |
| Orders 2,4,6 | PASS | All labelled odd-degree graphs and all initial states; verified by bundled Python script in release preparation |
| Eight-vertex exhaustive result | PASS, computational evidence | Two bundled C++ enumeration implementations and logs agree; an adversarial examiner separately reported an independent full re-enumeration. Original large C++ runs not rerun at v1.0 packaging. |
| Pair classification | PASS within `(n,m)=(8,13)` | Automorphism group size 2; four working initial states on canonical graph |
| Primary-source question match | PASS | arXiv:2507.04714v1 PDF, printed pp. 4 and 40 inspected; Section 6 all-time quantifier `forall t>=0` is distinct from 0-stable even-time definition |
| Prior art / scholarly novelty | INCONCLUSIVE | No exhaustive equivalence or priority audit is claimed |
| Peer review | NOT DONE | Adversarial AI-assisted checking is not editorial or journal peer review |

No statement of an unsolved problem being solved in priority order is intended; this release documents a checkable finite construction and delimited computational classification.

**Known limitations**

1. Minimal edge count thirteen is only established at eight vertices, not globally over every order.
2. The purely even-time universal 0-stable question is not refuted; 0-stable vertices are present in the witness.
3. The exhaustive-search classification is computer-assisted and requires reproducing or independently checking the provided programs.
4. A future identification of an equivalent earlier result may change scholarly novelty attribution.
5. The original internal v0.4 files are not altered: the public edition v1.0 changes only editorial presentation and rights wording, and reuses the original computational evidence.

**Source question**: Benjamini, Zakharov, Zhukovskii, *Majority dynamics on finite trees*, arXiv:2507.04714v1, doi:10.1002/rsa.70092.
