N, M, *X = map(int, open(0).read().split())
ans = max(0, min(X[1::2]) - max(X[::2]) + 1)
print(ans)
