N = int(input())  # 1 <= N <= 100
cake = N // 4
donuts = N // 7
calcs = False
for i in range(cake + 1):
  for j in range(donuts + 1):
    s = i * 4 + j * 7
    if s == N:
      calcs = True
      break
print("Yes" if calcs else "No")
