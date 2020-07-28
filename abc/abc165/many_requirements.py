# similar problems 
# https://qiita.com/u2dayo/items/386142030a70d2db4e58

"""
The array A
1<=A1<=A2....AN<=M
is like
◯◯|◯||◯||◯|◯|◯◯||◯◯
◯=10
|=9

so, the above means 19C9=92378 (on google input 19 choose 9)
The number of pattern of A array is less, so full search is possible.
"""
N, M, Q = map(int, input().split())
cond = []
for i in range(Q):
  a, b, c, d = map(int, input().split())
  cond.append((a - 1, b - 1, c, d)) # for reference index -1 from a and b

def dfs(A, head):
  """
  E.g. N=3, M=4
       a,b,c,d
       1 3 3 100
       1 2 2 10
       2 3 2 10

  dfs([1],1)->dfs([1,1],1)->dfs([1,1,1],1)->return score=0
                          ->dfs([1,1,2],2)->return score=0 
                          ->dfs([1,1,3],3)->return score=10
                          ->dfs([1,1,4],4)->return score=100
            ->dfs([1,2],2)->dfs([1,2,2],2)->return score=0
                          ->dfs([1,2,3],3)->return score=0
                          ->dfs([1,2,4],4)->return score=110
                          .......
  """
  #print(A, head)
  if len(A) == N:
    score = 0
    for a, b, c, d in cond:
      if A[b] - A[a] == c:
        score += d
    #print(f'score: {score}')
    return score
  ans = 0 
  for n in range(head, M + 1):
    ans = max(ans, dfs(A + [n], n))
  return ans
print(dfs([1], 1))
