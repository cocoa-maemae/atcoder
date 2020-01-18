N = input()
H = map(int, input().split())
last_h = float('inf')
cnt, ans = -1, 0
for h in H:
    if last_h >= h:
        # count to move
        cnt += 1
    else:
        # update answer
        if ans < cnt:
            ans = cnt
        # reset
        cnt = 0
    # height completed to be passed
    last_h = h
# check the last cnt and update answer
print(ans if ans > cnt else cnt)
"""
E.g.
5
10 4 8 7 3

10 can move only once, because 4 is lower than 8.
8->7->3 is enabled.
"""
