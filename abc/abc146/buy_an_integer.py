A, B, X = map(int, input().split())
# price can buy
ok = 0
# price can not buy
ng = 10 ** 9 + 1
# binary search
while ng - ok > 1:
  # Firstly check mid is available or not
  mid = (ok + ng) // 2
  # can buy
  if A * mid + B * len(str(mid)) <= X:
    ok = mid
  # can not buy
  else:
    ng = mid
print(ok)
