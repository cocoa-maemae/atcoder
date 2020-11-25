r1, c1 = map(int,input().split())
r2, c2 = map(int,input().split())
r = r2 - r1
c = c2 - c1
if (r, c) == (0, 0):
  print(0)
elif r == c or r == -c or abs(r) + abs(c) <= 3:
  print(1)
elif (r ^ c ^ 1) & 1 or abs(r) + abs(c) <= 6 or abs(r + c) <= 3 or abs(r - c) <= 3:
  print(2)
else:
  print(3)

"""
Move conditions
A: a+b=c+d
B: a-b=c-d
C: abs(a-c)+abs(b-d)<=3

If combined A,B and C, 3 is the maximum answer.
To determine 0,1,2 is OK.
See https://atcoder.jp/contests/abc184/editorial/339

The answer is 0, start and destination are same.
The answer is 1, start and destination are same as the condition of problem move condition.
The answer is 2, 
  the combination is the below.
  A,B
  A,C
  B,C
  C,C


"""
