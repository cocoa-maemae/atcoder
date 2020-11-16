from math import sqrt
N = int(input())
ans = set()
for n in range(1, int(sqrt(N)) + 1):
  if N % n == 0:
    ans.add(n)
    ans.add(N // n)
for a in sorted(ans):
  print(a)

"""
if N%X==0, N/X is also divisor

E.g.
N=24
divisors=1,2,3,4,6,8,12,24
1*24=3*8=4*6

N=4
divisors=1,2,4
care abount duplication print 2
"""
