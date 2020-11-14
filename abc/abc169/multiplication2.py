N = int(input())
A = list(map(int, input().split()))
THRESHOLD = 10 ** 18
if 0 in A:
  print(0)
  exit()
prod = 1
for i in range(N):
  prod *= A[i]
  if prod > THRESHOLD:
    print(-1)
    exit()
print(prod)
