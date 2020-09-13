S = str(input())
T = str(input())
if T in S:
  print(0)
  exit()
ans, substr = 0, ""
for i in range(len(S) - len(T) + 1):
  substr = S[i: i + len(T)] # if S=cabacc and T=abc, substr=cab,aba,bac,acc
  cnt = 0
  for s, t in zip(substr, T):
    # if substr=cab,aba,bac,acc, T=abc
    # cnt=0,2,1,2
    if s == t:
      cnt += 1
  ans = max(ans, cnt)
  if ans == len(T) - 1: # minimum
    break
print(len(T) - ans)
