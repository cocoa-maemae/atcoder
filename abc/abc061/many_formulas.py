
# solution by bit full search
S = input()
blank_cnt = len(S) - 1
ans = 0
for i in range(2 ** blank_cnt):
  formula = S[0]
  for j in range(blank_cnt):
    if (i >> j) & 1:
      formula += "+" + S[j + 1]
    else:
      formula += S[j + 1]
  ans += sum(list(map(int, formula.split("+"))))
print(ans)

"""
bit full search
1<=S<=10, so the maximum O(n) is 2**9

E.g. S=125
1{a}2{b}5
2 pattern(0 or 1) * the number of selects
=2**2

i j (i>>j)&1  formula
---------------------
0 0   0    
0 1   0       125
1 0   1
1 1   0       1+25
2 0   0 
2 1   1       12+5
3 0   1     
3 1   1       1+2+5

"""
