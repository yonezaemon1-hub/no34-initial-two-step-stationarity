"""No.34: a self-contained, standard-library verifier of a finite mathematical counterexample.
Python 3.12+; no dependencies; no network access.
"""
import json
from pathlib import Path

w = json.loads((Path(__file__).parent / "witness.json").read_text(encoding="utf-8"))
N = len(w["vertices"])
assert w["vertices"] == list(range(N)) and N == 8
adj = [set() for _ in range(N)]
for u, v in w["edges"]:
    assert 0 <= u < v < N and v not in adj[u]
    adj[u].add(v)
    adj[v].add(u)
assert len(w["edges"]) == 13
assert all(len(a) % 2 == 1 for a in adj), "All degrees must be odd to remove tie ambiguity"
assert sorted(len(a) for a in adj) == [1,3,3,3,3,3,5,5]

def advance(state):
    return tuple(1 if sum(state[j] for j in adj[i]) > 0 else -1 for i in range(N))

state = tuple(1 if v in w["initial_positive_vertices"] else -1 for v in range(N))
trace = []
for t in range(9):
    trace.append(state)
    state = advance(state)

assert [list(i for i, bit in enumerate(s) if bit == 1) for s in trace] == w["expected_trace_positive_vertices"]
assert trace[-1] == tuple([1] * N) and advance(trace[-1]) == trace[-1]
first_t = [next((t for t in range(len(trace) - 2) if trace[t][v] != trace[t+2][v]), None) for v in range(N)]
assert first_t == w["first_witness_t_by_vertex"]
assert all(t is not None for t in first_t), "A vertex is two-step stable from t=0"
print("PASS: 8 vertices, 13 edges, all vertex degrees odd; no vertex is two-step stable from t=0.")
print("First violating t per vertex:", first_t)
for t,s in enumerate(trace):
    print(f't={t}: ' + ''.join('+' if c==1 else '-' for c in s))
