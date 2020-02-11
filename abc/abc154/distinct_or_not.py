N = int(input())
A = input().split()
if len(A) == len(set(A)):
  print('YES')
else:
  print('NO')
