mod = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))
sum_of_all = sum(A) ** 2
sum_of_diagonal = 0
for i in range(N):
  sum_of_diagonal += A[i] ** 2
print((sum_of_all - sum_of_diagonal) // 2 % mod)

"""
if A=3,1,4

  3 1 4
  -----
3|9 3 12
1|3 1 4
4|12 4 16

answer: sum of all - sum of diagonal // 2

sum of all = (3+1+4)^2
sum of diagonal = 3^2+1^2+4^2
"""
