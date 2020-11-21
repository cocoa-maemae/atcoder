X, N = map(int, input().split())
P = list(map(int, input().split()))
for d in range(X + 1):
  for s in [-1, 1]:
    a = X + s * d
    if P.count(a) == 0:
      print(a)
      exit(0)
