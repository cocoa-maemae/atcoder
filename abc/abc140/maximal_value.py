N = int(input())
B = list(map(int, input().split()))
A = []
A.append(B[0])
for i in range(N - 2):
    A.append(min(B[i], B[i + 1]))
A.append(B[-1])
print(sum(A))
