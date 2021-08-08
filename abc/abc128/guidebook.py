N = int(input())
a = []
for i in range(N):
  S, P = input().split()
  a.append([S, -int(P), i + 1])
  a.sort()
for i in range(N):
  print(a[i][2])
