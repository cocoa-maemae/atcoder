N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]
from itertools import product
ans = 0
for dish_combination in product(*CD): # O(2^K)
  tmp = 0
  dishes = [0] * N # O(N)
  for c in dish_combination: # O(K)
    dishes[c - 1] += 1 # save cd combination as index of list
  for i in range(M): # O(M)
    if dishes[AB[i][0] - 1] > 0 and dishes[AB[i][1] - 1] > 0:
      tmp += 1
  ans = max(ans, tmp)
print(ans)

"""
K is less, so try all K combination patterns.
O(2^K*(N+M+K))
"""
