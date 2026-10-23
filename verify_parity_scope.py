"""Finite parity-scope audit; self-contained, standard-library only."""
from pathlib import Path
import json

w = json.loads(Path(__file__).with_name("witness.json").read_text("utf-8"))
n = len(w["vertices"])
assert n == 8
N = [set() for _ in range(n)]
for u,v in w["edges"]:
    N[u].add(v); N[v].add(u)
assert all(len(z)%2 for z in N)

def update(x):
    return tuple(1 if sum(x[v] for v in N[u])>0 else -1 for u in range(n))

x=tuple(1 if i in w["initial_positive_vertices"] else -1 for i in range(n))
trace=[]
for t in range(9):
    trace.append(x)
    x=update(x)
assert trace[7] == trace[8] and update(trace[8])==trace[8]

# The finite trace is complete, because the all-positive state from time 7 is fixed.
sets=[]
for parity in (0,1):
    stable={v for v in range(n) if all(trace[t][v]==trace[t+2][v] for t in range(parity,7,2))}
    sets.append(stable)
assert sets[0] == {0,2,6}, sets
assert sets[1] == {1,3,4,5,7}, sets
assert not (sets[0]&sets[1])
first=[next(t for t in range(7) if trace[t][v]!=trace[t+2][v]) for v in range(n)]
assert first == [1,0,3,0,4,0,5,6]
print("PASS: 0-stable (even t) vertices",sorted(sets[0]))
print("PASS: 1-stable (odd t) vertices",sorted(sets[1]))
print("PASS: no 0-stationary vertex; exact negation of §6.1 formal question")
