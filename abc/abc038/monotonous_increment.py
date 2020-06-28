# greedy
# similar like ABC152 C - Low Elements
N = int(input())
A = list(map(int, input().split()))
ans, tmp = 1, 1
for i in range(1, N):
  if A[i - 1] < A[i]:
    tmp += 1
  else:
    tmp = 1
  ans += tmp
print(ans)
"""
condition is l<=r, so l=r case must be counted.

E.g.
tmp 1 2 3 1 1
ans 1 3 6 7 8

If A=[1,2,3]
(i)If includes 3 numbers
(l,r)=(1,3)

(ii)If includes 2 numbers
(l,r)=(1,2),(2,3)

(iii)If includes 1 number
(l,r)=(1,1),(2,2),(3,3)
"""
