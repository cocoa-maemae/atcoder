N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = ['Yes' if A[i] > A[i - K] else 'No' for i in range(K, N)]
print("\n".join(ans))


"""
E.g.
N=5 K=3
A=96 98 95 100 20

3 term score: 96*98*95
4 term score: 98*95*100
5 term store: 95*100*20

When comprares scores between 3 term and 4 term, 96 and 100 is OK since 98*95 is same.
When comprares scores between 4 term and 5 term, 98 and 20 is OK since 95*100 is same.

To recap, just compare A[i] and A[i - K] is OK.
"""
