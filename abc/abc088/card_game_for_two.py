N = int(input())
A = list(map(int, input().split()))
# Sort by desc
A.sort(reverse=True)
# Alice gets from the biggest number
# E.g. 5 4 3 2 1
# Alice gets 5 3 1
# Bob gets 4 2
print(sum(A[::2]) - sum(A[1::2]))
