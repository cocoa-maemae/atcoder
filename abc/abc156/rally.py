N = int(input())
X = list(map(int, input().split()))
"""
Not consider coord < min(X) and coord > max(X)
average of min(X) and max(X) is the minimum diff from x1,x2....xn
"""
avg = round(sum(X) / N)
print(sum([(x - avg) ** 2 for x in X]))
