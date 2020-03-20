# similar like ABC152 C - Low Elements
N = int(input())
A = map(int, input().split())
tmp, pre, ans = 0, 0, 0
for a in A:
  if pre < a:
    tmp += 1
  else:
    tmp = 1
  pre = a
  ans += tmp
print(ans)
"""
E.g.
a   1 2 3 2 1
tmp 1 2 3 1 1
ans 1 3 6 7 8
"""
