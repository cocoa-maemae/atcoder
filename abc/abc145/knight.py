X, Y = map(int, input().split())
def comb(n, r, mod=10 ** 9 + 7):
  n1 = n + 1
  r = min(n, n - r)
  numer = denom = 1
  for i in range(1, r + 1):
    numer = numer * (n1 - i) % mod
    denom = denom * i % mod
  return numer * pow(denom, mod - 2, mod) % mod
# X + Y coordinates increase by 3 per one move. X + Y should be factor of 3
ans = 0
if (X + Y) % 3 == 0 and 2 * Y >= X and 2 * X >= Y:
  # (i+1,j+2) count is x, (i+2,j+1) count is y, x+yCx is the answer
  # solve the below equations、get x = 2Y − X / 3，y = 2X − Y / 3
  # x + 2y = X, 2x + y = Y
  x, y = (2 * Y - X) // 3, (2 * X - Y) // 3
  ans = comb(x + y, x)
print(ans)
