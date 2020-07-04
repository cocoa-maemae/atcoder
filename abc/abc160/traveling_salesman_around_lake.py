K, N = map(int, input().split())
A = list(map(int, input().split()))
d = [A[i + 1] - A[i] for i in range(N - 1)]
d.append(K + A[0] - A[N - 1])
print(sum(d) - max(d))

"""
E.g.
K=20, N=3
A=5,10,15

Remove the longest diff within N+1 interval
  ------5
  |     |
  |     |
  |     |
  |     |
  |     |
 15-----10
           
0-----5-----10-----15-----20-----5
     A[0]   A[1]   A[2]   K      K+A[0]
           
"""
