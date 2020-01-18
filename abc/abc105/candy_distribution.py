from collections import Counter
from itertools import accumulate
N, M = map(int, input().split())
# select several boxes in A, and distribute to children equally
A = map(int, input().split())
acc = [0]
# accumulate calculate cumulative sum 
# E.g. [4, 1, 5] -> [4, 5, 10]
# Al + ... + Ar = ACCr - ACCl-1(ACC0 = 0) 
acc.extend(accumulate(A))
# Counter counts the number of appearence of elements
# M means the number of children
cnt = Counter(a % M for a in acc)
# Al + ... + Ar must be multiple of M equals to ACCr - ACCl-1 must be also multiple of M
# v * (v - 1) // 2 means vC2
ans = sum(v * (v - 1) // 2 for v in cnt.values())
print(ans)

"""
E.g.
M = 3
i                   1  2  3  4  5
a                   5  2  5  2  1
cumulative sum   0  5  7 12 14 15
sum mod M        0  2  1  0  2  0

answer pattern
if mod=0, 3 pattern. select 2 from 3 of mod=0(=3C2)
5+2+5
2+1
5+2+5+2+1
if mod=1, not consider
if mod=2, 1 pattern. select 2 from 2 of mod=2(=2C1)
2+5+2
"""
