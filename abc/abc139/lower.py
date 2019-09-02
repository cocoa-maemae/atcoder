N = input()
H = map(int, input().split())
last_h = float('inf')
cnt = -1
ans = 0

for h in H:
    if h <= last_h:
        # count to move
        cnt += 1
    else:
        # update answer
        ans = max(ans, cnt)
        # reset
        cnt = 0
    # height completed to be passed
    last_h = h

# check the last cnt and update answer
ans = max(ans, cnt)
print(ans)
