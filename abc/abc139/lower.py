N = int(input())
H = list(map(int, input().split()))
cnt, ans = 0, 0
for i in (1, N):
    if H[i - 1] >= H[i]:
        # count to move
        cnt += 1
    else:
        # update answer(faster than max)
        if ans < cnt:
            ans = cnt
        # reset
        cnt = 0
# check the last cnt and update answer
print(ans if ans > cnt else cnt)
"""
E.g.
5
10 4 8 7 3

10 can move only once, because 4 is lower than 8.
8->7->3 is enabled.
"""
