N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]
# sort by Ci desc
BC = sorted(BC, key=lambda x: (x[1]), reverse=True)
cards = []
for b, c in BC:
  if len(cards) >= N:
    break
  # same list.append
  cards += [c] * b
A += cards
A.sort(reverse=True)
print(sum(A[:N]))

"""
See https://www.youtube.com/watch?v=SS6kW-d-rJ0

E.g.1.
3 2
5 1 4
2 3
1 5

sorted BC=[[1, 5], [2, 3]]
cards+=[c]*b => [5]*1=[5] [3]*2=[3,3]=>[5,3,3]
As priority queue, append all the cards to list
And extract by desc using sort
A=[5,1,4,5,3,3]
A.sort(reverse=True)=>[5,5,4,3,3,1]


E.g.2.
10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4

sorted BC=[[4,30],[3,10],[1,4]]
cards+=[c]*b => [30,30,30,30,10,10,10,4]
As priority queue, append all the cards to list
And extract by desc using sort
A=[1,8,5,7,100,4,52,33,13,5,30,30,30,30,10,10,10,4]
A.sorted(revers=True)=[100,52,33,30,30,30,30,3,10,10,10,8,7,5,5,,4,1]
"""
