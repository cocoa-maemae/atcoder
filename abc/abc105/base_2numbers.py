N = int(input())
a = []
if N == 0:
    a = ["0"]
while N != 0:
    a.append(str(N % 2)) # N mod 2 is same as N mod -2 because remainder is 1 or 0
    N =  -(N // 2)
print("".join(list(reversed(a))))
