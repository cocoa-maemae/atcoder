N, M = map(int, input().split())
A = list(map(int, input().split()))
A += [0, N + 1] # interval till N+1 is 0
A.sort()
if len(A) == N + 2: # mass count equals blue count, white count is 0
  print(0)
  exit()
# A[i+1]-A[i]-1 means white intervals
k = min([A[i + 1] - A[i] - 1 for i in range(M + 1) if A[i + 1] - A[i] - 1 > 0]) # white interval 0 is enabled
# if interval is not divided by k, 
ans = sum([((A[i + 1] - A[i] - 1) + (k - 1)) // k for i in range(M + 1)])
print(ans)

"""
E.g.1
5 2
1 3
●◯●◯◯

E.g.2
11 2
4 9
◯◯◯●◯◯◯◯●◯◯

Seperate by blue
◯◯◯->2*k
◯◯◯◯->2*k
◯◯->1*k
In this case k is 2.
The minimum of white length is k.

"""
