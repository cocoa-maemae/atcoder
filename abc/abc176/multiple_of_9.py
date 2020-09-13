N = input()
cnt = 0
for i in range(10):
  cnt += i * N.count(str(i))
print("Yes" if cnt % 9 == 0 else "No")
