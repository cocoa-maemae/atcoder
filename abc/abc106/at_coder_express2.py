import sys
from itertools import accumulate as acc

s = sys.stdin.readlines()
N, M, _ = map(int, s[0].split())
X = [[0] * N for _ in [0] * N]
for L, R in (map(int, e.split()) for e in s[1:M + 1]): X[L - 1][R - 1] += 1
S = [tuple(acc(reversed(s))) for s in zip(*(acc(x) for x in X))]
print('\n'.join(map(str, (S[q - 1][N - p] for p, q in (map(int, e.split()) for e in s[M + 1:])))))
