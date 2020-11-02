A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
A = A1 + A2 + A3
N = int(input())
s = set() # index of A
for _ in range(N):
  b = int(input())
  if b in A:
    s |= {A.index(b)} 
# bingo index list of set
bingo = [{0, 1, 2}, {0, 3, 6}, {0, 4, 8}, {1, 4, 7}, {2, 4, 6}, {2, 5, 8}, {3, 4, 5}, {6, 7, 8}]

# compare set
print(['No','Yes'][any(b <= s for b in bingo)])
"""
E.g.
set1={8,0,3,4}
set2={0,4,8}
set1>=set2 shows True
"""

"""
print(["No","Yes"][True]) shows Yes, becuase True is 1
print(["No","Yes"][False]) shows No, becuase True is 0
"""

"""
Check the problems
B - Trick or Treat
"""
