N = int(input())
aoki_votes, takahashi_votes = 0, 0
d = []
for _ in range(N):
  A, B = map(int, input().split())
  aoki_votes += A
  d.append(2 * A + B)
d.sort()
cnt = 0
while aoki_votes >= takahashi_votes:
  takahashi_votes += d.pop()
  cnt += 1
print(cnt)

"""
If A<T, takahashi is stronger than aoki.
Same as A-T<0
Control A-T

E.g.
4
2 1
2 2
5 1
1 3

Aoki's total votes=10(2+2+5+1)

4   If takahashi speeches,
2 1 Aoki-2,takahashi+3 For Aoki -5votes
2 2 Aoki-2,takahashi+4 For Aoki -6votes
5 1 Aoki-5,takahashi+6 For Aoki -11votes
1 3 Aoki-1,takahashi+4 For Aoki -5votes

If Takahashi speeches, Aoki's votes decrease like the below.
2 1->10-5(=2*2+1)
2 2->10-6(=2*2+2)
5 1->10-11(=5*2+1)
1 3->10-5(=1*2+3)

So sort 2A+B and minus from aoki's all votes.
"""
