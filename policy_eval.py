import numpy as np

A, D = [(1, 0), (-1, 0), (0, -1), (0, 1)], {(1, 0): '↓', (-1, 0): '↑', (0, -1): '←', (0, 1): '→'}

class Grid:
    def __init__(s, n=4): s.n, s.v = n, np.zeros((n, n))

    def step(s, p, a):
        if p in [(0, 0), (s.n-1, s.n-1)]: return p, 0
        return tuple(np.clip(np.add(p, a), 0, s.n-1)), -1

    def update(s, k):
        for _ in range(k): s.v = np.array([[sum(0.25 * (r + s.v[n]) for a in A for n, r in [s.step((i, j), a)]) 
                                            for j in range(s.n)] for i in range(s.n)])

    def show(s): print("\n".join(" ".join(f"{v:6.2f}" for v in r) for r in s.v), "\n")

    def policy(s):
        print("\n".join(" ".join("".join(D[a] for a in A if s.v[i, j] < s.v[tuple(np.clip(np.add((i, j), a), 0, s.n-1))])
                        if (i, j) not in [(0, 0), (s.n-1, s.n-1)] else " X " for j in range(s.n)) for i in range(s.n)))

g = Grid(4)
for k in [1, 2, 3, 1000, 20000]: g.update(k); print(f"\nAfter {k} Steps:"); g.show()
print("Final Policy Directions:"); g.policy()
