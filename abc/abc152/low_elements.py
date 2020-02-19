N = int(input())
P = list(map(int, input().split()))
cnt = 1 # P[0] is counted forcely
min = P[0]
for p in P:
  # (1≤j≤i),Pj=>Pi
  if min > p:
    min = p
    cnt += 1
print(cnt)
