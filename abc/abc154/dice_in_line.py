from itertools import accumulate
N, K = map(int, input().split())
P = list(map(int, input().split()))
acc = [0] + list(accumulate(P))
"""
If, acc: [0,1,3,5,9,14]
for a, b in zip(acc, acc[K:]):
  print(a, b)
is (0,5),(1,9),(3,14)
"""

"""
The below is mostly same as

ans = 0
for a, b in zip(acc, acc[K:]):
  exp = (b - a + K) / 2
  ans = max(exp, ans)
print(ans)
"""
print((max(b - a for a, b in zip(acc, acc[K:])) + K) / 2)

"""
expecation of 1~p is (1+p)/2

E.g.
K=3
P:     [1,2,2,4,5]
acc: [0,1,3,5,9,14]
exp: [5-0+3/2,9-1+3/2,14-3+3/2] 

if calculate expectation of [1,2,2],
exp=(1+1)/2+(1+2)/2+(1+2)/2=(1+1+1)+(1+2+2)/2
   =K+(5-0)/2 
       5-0 means diff of acc
if calculate expectation of [2,2,4],
exp=(1+2)/2+(1+2)/2+(1+4)/2=(1+1+1)+(2+2+4)/2
   =K+(9-1)/2
       9-1 means diff of acc
if calculate expectation of [2,4,5],
exp=(1+2)/2+(1+4)/2+(1+5)/2=(1+1+1)+(2+4+5)/2
   =K+(14-3)/2
       14-3 means diff of acc
"""
