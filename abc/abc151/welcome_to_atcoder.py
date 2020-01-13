from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 6)
input = stdin.readline
N, M = map(int, input().split())
ac = [False] * N # index means p
wa = [0] * N # index means p
wa_cnt = 0
for i in range(M):
  p, s = input().split()
  p = int(p) - 1 # index starts from 0
  if ac[p] is False and s == "AC":
    wa_cnt += wa[p]
    ac[p] = True
  elif s == "WA":
    wa[p] += 1
print(ac.count(True), wa_cnt)
