A, B = map(int, input().split())
_MAX_PRICE = 1001
for n in range(1, _MAX_PRICE):
  if int(n * 0.08) == A and int(n * 0.1) == B:
    print(n)
    exit()
print(-1)
