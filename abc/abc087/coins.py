A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for a in range(A + 1):
    for b in range(B + 1):
        q = (X - (500 * a + 100 * b)) / 50
        if q >= 0 and q <= C:
            ans += 1
print(ans)
