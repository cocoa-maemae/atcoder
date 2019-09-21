import sys
N, K, Q = map(int, input().split())
A = (int(x) for x in sys.stdin.read().split())
score = [K - Q] * (N + 1)
for a in A:
    score[a] += 1
ans = "\n".join("No" if s <= 0 else "Yes" for s in score[1:])
print(ans)
