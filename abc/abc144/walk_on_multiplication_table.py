N = int(input())
from math import sqrt
# if n=10, return[(1,10),(2,5)]
def get_divisors(n):
    divs = []
    #for i in range(1, int(n ** 0.5) + 1):
    for i in range(1, int(sqrt(n)) + 1): # int(sqrt(10))=3
        #if not n % i:
        if n % i == 0: # if n=10,i=1,n%i==0, i=2,n%i==0
            divs.append((i, n // i))
    return divs
     
ans = float("inf")
d = get_divisors(N)
for x, y in d:
    # move count from (1, 1) to (a, b) is a+b-2
    ans = min(ans, x + y - 2)
print(ans)
