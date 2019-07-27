N = int(input())  # 1 <= N <= 100
b = 1
for i in range(25):  # the limit 4 * 25 = 100
    b |= b << 4
for i in range(15):  # the limit 7 * 15 = 105
    b |= b << 7
ans = "Yes" if (b >> N) & 1 else "No"
print(ans)
