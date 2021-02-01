N = int(input())
A = list(map(int, input().split())) + [0]
candidates = [-1]
ans = 0
for i in range(N + 1):
  while A[candidates[-1]] > A[i]: # candidates[-1] means the last element of candiates
    print(i,candidates[-1],A[candidates[-1]])
    ans = max(ans, (i - candidates[-2] - 1) * A[candidates[-1]]) # candidates[-2] means the second of last candidates
    candidates.pop()
    print(candidates)
  candidates += [i] # add index
print(ans)

"""
Orange like the below,
oooo oo oo ooo o oo o ooo ooooo oooo

X is the minimum value between l and r.
If try all l and r, 0(N^2/2). This is difficult.

E.g.
6
2 4 4 9 4 9

4>9,i=3,candidates=[-1,0,1,2,3]
ans=max(0,(3-2-1)*9)
candidates=[-1,0,1,2]


"""
