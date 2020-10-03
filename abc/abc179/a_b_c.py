N = int(input())
ans = 0
for a in range(1, N):
  ans += (N - 1) // a
print(ans)

"""
If A and B are decided, C is also decided
A*B+C=N
A*B=N-C(C>1)
If N=6,A*B=5 then C=1 valid
   N=6,A*B=3 then C=3 valid
   N=6,A*B=6 then C=0 not valid.
So calculate combination count of A,B with condition like A*B<=N-1, C is also decided.

If A is fixed, combination count of B=(N-1)//A
E.g.
A*B<=N-1 
N=100,A=3,B=1~33 combination count of B is 100//3

"""
