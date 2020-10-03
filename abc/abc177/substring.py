S = str(input())
T = str(input())
if T in S:
  print(0)
  exit()
max_same_char_cnt, substr = 0, ""
for i in range(len(S) - len(T) + 1):
  substr = S[i: i + len(T)] # if S=cabacc and T=abc, substr=cab,aba,bac,acc
  same_char_cnt = 0
  for s, t in zip(substr, T):
    # if substr=cab,aba,bac,acc, T=abc
    # cnt=0,2,1,2
    if s == t:
      same_char_cnt += 1
  max_same_char_cnt = max(max_same_char_cnt, same_char_cnt)
  if max_same_char_cnt == len(T) - 1: # minimum replace cnt
    break
print(len(T) - max_same_char_cnt)
