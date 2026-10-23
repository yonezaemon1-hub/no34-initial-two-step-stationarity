"""Independently check witness, graph automorphisms and four initial states.
Pure Python 3.12; does not import v0.1 code or require third-party packages.
"""
import itertools
from pathlib import Path
import json

w = json.loads(Path(__file__).with_name("witness.json").read_text("utf-8"))
N=8
edge_set={frozenset(e) for e in w['edges']}
assert len(edge_set)==13 and len({v for e in edge_set for v in e})==N
neighbours={u: {v for e in edge_set if u in e for v in e if v != u} for u in range(N)}
assert [len(neighbours[u]) for u in range(N)] == [3,5,3,5,3,3,3,1]

def f(x):
    return sum((1<<u) for u in range(N)
               if sum((x >> v) & 1 for v in neighbours[u]) > len(neighbours[u])//2)

def good(initial):
    seen=set()
    x=initial
    mask=(1<<N)-1
    while x not in seen:
        seen.add(x)
        mask &= ~(x ^ f(f(x))) & ((1<<N)-1)
        x=f(x)
    return mask == 0

states=[x for x in range(1<<N) if good(x)]
assert states == [71,102,153,184], states
x0=sum(1<<v for v in w['initial_positive_vertices'])
assert x0 == 71
traj=[]
x=x0
for _ in range(9):
    traj.append([u for u in range(N) if x & (1<<u)])
    x=f(x)
assert traj == w['expected_trace_positive_vertices']

# All 8! label permutations; a graph automorphism preserves the edge set.
automorphisms=[]
for perm in itertools.permutations(range(N)):
    if {frozenset((perm[u], perm[v])) for e in edge_set for u,v in [tuple(e)]} == edge_set:
        automorphisms.append(perm)
assert len(automorphisms)==2, automorphisms

# Explicit orbit from 71 under Aut(G) and global sign reversal.
orb=set()
for perm in automorphisms:
    xx=sum((1<<perm[u]) for u in range(N) if x0 & (1<<u))
    orb.update([xx, ((1<<N)-1)^xx])
assert orb==set(states), (orb,states)
print('PASS witness trace, degrees and no two-step stationary vertex')
print(f'PASS graph automorphism group order = {len(automorphisms)}; orbit of graph under S8 = {40320//len(automorphisms)}')
print(f'PASS exactly {len(states)} initial states for this labelled graph: {states}')
print('PASS all four states are symmetry-equivalent using graph automorphism and global spin reversal')
