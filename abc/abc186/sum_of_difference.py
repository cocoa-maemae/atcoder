N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
t, ans = 0, 0
for i in range(N - 1, 0, -1):
  # if sorted A=5 2 1, t=1 3
  t += A[i]
  # if sorted A=5 2 1, ans=(2*1-1)+(5*2-3)
  ans += A[i - 1] * (N - i) - t
print(ans)

"""
Firstly sort A, and not need to consider abs
A=5 1 2->5 2 1

Sum like the below
5-1
5-2
5*2-(1+2)

2-1
2*1-1

5*2-(1+2) + 2*1-1
"""
