N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
best_score = {"r": P, "s": R, "p": S}
ans = 0
# Initially, plus best scores till K.
# Because anything is OK till K count.
for i in range(K):
  ans += best_score[T[i]]
  # After K count
  for i in range(K, N):
    # Check i - K count.
    if T[i - K] == T[i]:
      # draw
      T[i] = ""
      continue
    ans += best_score[T[i]]
print(ans)
