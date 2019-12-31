# 残っているレンガの中で左から i 番目のものに書かれた整数が i であるとき、すぬけさんは満足します。
# After break brick must be like 1 2 3.
N = int(input())
A = list(map(int, input().split()))
cnt, i = 0, 1
for a in A:
  if a == i:
    # search brick like 1,2,3...
    i += 1
  else:
    # break
    cnt += 1
print(cnt if cnt != N else -1)
