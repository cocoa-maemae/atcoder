import math

N = int(input())
A = list(map(int, input().split()))
ans = float("inf")
for a in A:
    ans = min(ans, len(bin(a)) - bin(a).rfind("1") - 1)
print(round(ans))
