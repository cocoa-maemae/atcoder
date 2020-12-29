X, N = map(int, input().split())
if N == 0:
  print(X)
  exit()
P = list(map(int, input().split()))
while True:
  for s in [-1, 1]:
    a = X + s * d
    if P.count(a) == 0:
      print(a)
      exit(0)
  d+=1

"""
a=X+s*d
a=X,X−1,X+1,X−2,X+2....
"""
