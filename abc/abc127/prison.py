N, M, *X = map(int, open(0).read().split())
# X[1::2] extract only number of even index
# X[::2] extract only number of odd index
ans = max(0, min(X[1::2]) - max(X[::2]) + 1)
print(ans)
