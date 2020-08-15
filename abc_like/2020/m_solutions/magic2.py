A, B, C = map(int, input().split())
K = int(input())
# greedy
cnt = 0
while A >= B:
  B *= 2
  cnt += 1
while B >= C:
  C *= 2
  cnt += 1
if cnt <= K:
  print('Yes')
else:
  print('No')
