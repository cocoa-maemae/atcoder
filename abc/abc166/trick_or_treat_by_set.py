N, K = map(int, input().split())
sunuke_who_has_sweets = set()
for i in range(K):
  d = int(input())
  A = map(int, input().split())
  sunuke_who_has_sweets |= set(A)
print(N - len(sunuke_who_has_sweets))
