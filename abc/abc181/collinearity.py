N = int(input())
coordinates = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
  slopes = []
  for j in range(i + 1, N):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[j]
    slope = "0" if x1 == x2 else (y2 - y1) / (x2 - x1)
    if slope in slopes:
      print("Yes")
      exit()
    slopes.append(slope)
print("No")
