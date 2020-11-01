N, M, *HAB = map(int, open(0).read().split())
H, AB = [0] + HAB[:N], HAB[N:]
good = [False] + [True] * N
for a, b in zip(*[iter(AB)] * 2):
  if H[a] >= H[b]:
    good[b] = False
  if H[b] >= H[a]:
    good[a] = False
print(sum(good))

"""
Similar like 
C - Neq Min
C - Welcome to AtCoder
"""
