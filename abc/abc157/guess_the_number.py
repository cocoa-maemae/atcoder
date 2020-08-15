N, M = map(int, input().split())
SC = [input().split() for _ in range(M)]
ans = ["0"] * N
for s, c in SC:
  # check duplicated s
  if ans[int(s) - 1] != "0" and ans[int(s) - 1] != c:
    print(-1)
    exit()
  # check impossible case
  if N > 1 and s == "1" and c == "0":
    print(-1)
    exit()
  ans[int(s) - 1] = c
# replace head
if ans[0] == "0" and N > 1:
  ans[0] = "1"
print("".join(ans))
