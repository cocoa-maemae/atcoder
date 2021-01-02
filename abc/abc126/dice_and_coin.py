N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
  p, s = 1, i
  while s < K:
    p *= 0.5
    s *= 2
  ans += p / N
print(ans)

"""
E.g.
N=3,K=10
dice has 1,2,3

If back side appears, sunuke will lose.
Need that head appears continuously.

If dice is 1, initial score is 1.
And then, shake the coin.
score=1->2->4->8->16(>=K-1)
probability is 1/2**4=1/16

If dice is 2, initial score is 2.
And then, shake the coin.
score=2->4->8->16(>=K-1)
probability is 1/2**3=1/8

If dice is 3, initial score is 3.
And then, shake the coin.
score=3->6->12(>=K-1)
probability is 1/2**2=1/4

answer is (1/16+1/8+1/4)/3=7/48
"""
