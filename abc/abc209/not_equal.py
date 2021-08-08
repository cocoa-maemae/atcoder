N = int(input())
C = list(map(int, input().split()))
C.sort()
ans = 1
for i in range(N):
  ans = ans * (C[i] - i) % 1000000007
print(ans)

"""
If C=[100,100,100]
ans=100*99*98
A1 is 100(1~100) pattern
A2 is 100-1(exclude A1)=99 pattern
A3 is 100-2(exclude A1,A2)=98 pattern

So making answer formula, ans*=(Ci-i+1)
provided that C must be sorted by ascending.
"""
