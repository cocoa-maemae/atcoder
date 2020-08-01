N, K = map(int, input().split())
sunuke_and_sweets_cnt = [0] * N # index is sunuke, value is sweets count
for i in range(K):
  d = int(input())
  A = list(map(int, input().split()))
  for j in range(d):
    sunuke_and_sweets_cnt[A[j] - 1] = 1
ans = 0
for sweet in sunuke_and_sweets_cnt:
  if sweet == 0:
     ans += 1
print(ans)
