N, M, *HAB = map(int, open(0).read().split())
H, AB = HAB[:N], HAB[N:]
good = [True] * N
for a, b in zip(*[iter(AB)] * 2):
  if H[a - 1] >= H[b - 1]:
    good[b - 1] = False
  if H[b - 1] >= H[a - 1]:
    good[a - 1] = False
print(sum(good))
