X, Y = map(int, input().split())
for a in range(X + 1):
  b = X - a
  if 2 * a + 4 * b == Y:
    print("Yes")
    exit()
print("No")
