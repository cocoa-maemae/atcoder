N, K, *S = map(int, open(0).read().split())
# if 0 exist, the longest length is N
if 0 in S:
  print(N)
  exit()
# two pointers
prod, ans, fast_i = 1, 0, 0
for i in range(N):
  while fast_i < N:
    prod *= S[fast_i]
    if prod > K:
      # cache the index
      fast_i += 1
      break
    ans = max(ans, fast_i - i + 1)
    fast_i += 1
  prod //= S[i]
print(ans)
