N, A, B = map(int, input().split())
ans = 0

for n in range(N + 1):
    if A <= sum(list(map(int, str(n)))) <= B:
        ans += n
print(ans)
