S = list(input())
def dfs(S, i, last_s, sum): 
  if i == len(S):
    return sum + int(last_s)
  return dfs(S, i + 1, S[i], int(last_s) + sum) + dfs(S, i + 1, last_s + S[i], sum)
print(dfs(S, 1, S[0], 0))

# E.g. S=125
# dfs(125,1,1,0)->dfs(125,1+1,S[1],1+0)           +           dfs(125,1+1,1+S[1],0)
#                   ->dfs(125,2+1,S[2],2+1)+dfs(125,2+1,2+S[2],1)
#                     return 2+1+5         return +7
#
#               
#
#
