S = list(input())
def dfs(S, i, bind, ans): 
  if i == len(S):
    return ans + int(bind)
  return dfs(S, i + 1, S[i], int(bind) + ans) + dfs(S, i + 1, bind + S[i], ans)
print(dfs(S, 1, S[0], 0))
