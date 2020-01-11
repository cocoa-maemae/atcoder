N, M = map(int, input().split())
A = list(set(map(lambda x : int(x) // 2, input().split())))
def gcd(x, y):
  return x if y == 0 else gcd(y, x % y)
def lcm(x, y):
  return (x * y) // gcd(x, y)
l = A[0]
for a in A[1:]:
  l = lcm(l, a)
ans = (M // l + 1) // 2
for a in A[1:]:
  if (l // a) % 2 == 0:
    ans = 0
    break
print(ans)
