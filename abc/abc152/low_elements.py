N = int(input())
P = list(map(int, input().split()))
cnt = 1 # P[0] is counted forcely
min_num = P[0]
for p in P:
  if p < min_num:
    min_num = p
    cnt += 1
print(cnt)
