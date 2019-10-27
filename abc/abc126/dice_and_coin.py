import math
N, K = map(int, input().split())
ans = 0.
rate = 1./N
for i in range(N):
  if i + 1 >= K:
    ans += rate
  else:
    ans += rate * 0.5 ** math.ceil(math.log(K / (i + 1), 2))
print(ans)
