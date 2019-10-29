N = int(input())
from pprint import pprint     
def get_divisors(n):
    divs = []
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            divs.append((i, n // i))
    return divs
     
ans = float("inf")
d = get_divisors(N)
pprint(d)
for x, y in d:
    ans = min(ans, x + y - 2)
print(ans)
