N = int(input())
A = list(map(int, input().split())) + [-1]
stack = [-1] # index stack
ans = 0
for i in range(N + 1):
  # finally while sentence repeats at the end element -1
  while A[i] < A[stack[-1]]: # stack[-1] means the last element of candiates
    # (i-stack[-2]-1) means r-l. -1 is necessary because -1 is added.
    ans = max(ans, (i - stack[-2] - 1) * A[stack[-1]]) # stack[-2] means the second of last candidates
    stack.pop()
  stack += [i] # add i to list
print(ans)

"""
x is the minimum A between i=l and i=r

E.g.
6
2 4 4 9 4 9

A=[2,4,4,9,4,9,-1]
stack=[-1,0,1,2,3]

i=4,stack[-1]=3,A[stack[-1]]=9>A[i]
ans=max(0,(4-2-1)*9)=9
stack=[-1,0,1,2]

stack=[-1,0,1,2,4,5]

i=6,stack[-1]=5,A[stack[-1]]=9>A[i]
ans=max(9,(6-4-1)*9)=9
stack=[-1,0,1,2,4]

i=6,stack[-1]=4,9>0
ans=max(9,(6-2-1)*4)=12
stack=[-1,0,1,2]

i=6,stack[-1]=2,A[stack[-1]]=4>A[i]
ans=max(9,(6-1-1)*4)=16
stack=[-1,0,1]

i=6,stack[-1]=1,A[stack[-1]]=4>A[i]
ans=max(16,(6-0-1)*4)=20
stack=[-1,0]

If other language, the below is not TLE(But python is TLE)
ans = 0
for i in range(N):
    orange = A[i]
    for j in range(i, N):
        orange = min(orange, A[j])
        ans = max(ans, orange * (j - i + 1))
print(ans)
"""
