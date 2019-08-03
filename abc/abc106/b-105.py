from math import floor, sqrt

N = int(input())
ans = 0
# target is only odd number
for o in range(1, N + 1, 2):
    cnt = 0
    for n in range(1, 1 + floor(sqrt(o))):
        if o % n == 0:
            # number of measure is number of square root * 2
            cnt += 2
    if cnt == 8:
        ans += 1
print(ans)
