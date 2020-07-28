# solution by dfs
S = list(input())
def dfs(s, i): 
  print(s, i)
  if i == len(S) - 1:
    return sum(map(int, s.split("+")))
  return dfs(s + S[i + 1], i + 1) + dfs(s + "+" + S[i + 1], i + 1)
print(dfs(S[0], 0))

"""
E.g. S=125

dfs(1, 0)->dfs(12,1)                 +     dfs("1+2",1)
         ->dfs(125,2) + dfs("12+5",2)      ->dfs("1+25",2)  + dfs("1+2+5",2)
         ->return 125   ->return 17        ->return 26         ->return 8
"""
