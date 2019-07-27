N = int(input())
a = []
if N == 0:
    a = ["0"]
while N != 0:
    a.append(str(N % 2)) # N mod 2
    N = -(N - N % 2) // 2 # (N − (N mod 2)) // 2
print("".join(list(reversed(a))))
