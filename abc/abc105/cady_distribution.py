from collections import Counter
from itertools import accumulate

N, M = map(int, input().split())
A = map(int, input().split())
acc = [0]
acc.extend(accumulate(A))
acc = Counter(a % M for a in acc)
ans = sum(c * (c - 1) // 2 for c in acc.values())
print(ans)
