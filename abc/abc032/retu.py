N, K, *S = map(int, open(0).read().split())
# if 0 exist, the longest length is N
if 0 in S:
  print(N)
  exit()
# two pointers
prod, ans, right_i = 1, 0, 0
for i in range(N):
  while right_i < N:
    prod *= S[right_i]
    if prod > K:
      # cache the index
      right_i += 1
      break
    ans = max(ans, right_i - i + 1)
    right_i += 1
  prod //= S[i]
print(ans)
