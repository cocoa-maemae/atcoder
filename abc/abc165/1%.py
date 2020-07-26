X = int(input())
deposit, year = 100, 0
while deposit < X:
  deposit += deposit // 100
  year += 1
print(year)
