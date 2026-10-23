"""Independently enumerate ALL labelled simple graphs where every degree is odd.

For even n, edges among vertices 0..n-2 are free. The last n-1 edges
are uniquely determined by odd-degree requirements. The final vertex then
has odd degree by the handshake lemma. Exhaustive up to n=6.
Pure Python; no dependencies.
"""
from itertools import combinations


def enumerate_graphs(n):
    pairs = list(combinations(range(n-1), 2))
    for bits in range(1 << len(pairs)):
        adj = [set() for _ in range(n)]
        for k,(u,v) in enumerate(pairs):
            if bits & (1 << k):
                adj[u].add(v)
                adj[v].add(u)
        for v in range(n-1):
            if len(adj[v]) % 2 == 0:
                adj[v].add(n-1)
                adj[n-1].add(v)
        assert all(len(ns) % 2 for ns in adj)
        yield adj


def step(state, adj):
    return tuple(1 if sum(state[u] for u in ns) > 0 else -1 for ns in adj)


def all_have_at_least_one_initially_two_step_stable_vertex(state, adj):
    n = len(adj)
    # Initially any vertex could be stable. Eliminate whenever s(t) != s(t+2).
    alive = set(range(n))
    first = state
    second = step(first, adj)
    for _ in range(n * n + 4):
        third = step(second, adj)
        alive.difference_update(v for v in tuple(alive) if first[v] != third[v])
        if not alive:
            return False
        if first == third:  # the whole state is in a 1- or 2-cycle
            return True
        first, second = second, third
    raise RuntimeError('Unexpectedly long transient')

for n in (2,4,6):
    count = 0
    graphs = 0
    for adj in enumerate_graphs(n):
        graphs += 1
        for bits in range(1 << n):
            state = tuple(1 if bits & (1 << v) else -1 for v in range(n))
            count += 1
            assert all_have_at_least_one_initially_two_step_stable_vertex(state, adj), (n, adj, state)
    print(f'PASS n={n}: {graphs} labelled all-odd-degree graphs x {1<<n} states = {count} cases')
print('PASS: no counterexample on fewer than 8 vertices in the odd-degree setting')
