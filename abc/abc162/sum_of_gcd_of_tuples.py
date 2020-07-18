import collections
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)
K = int(input())
ans = 0
cnt = collections.defaultdict(int)
# count the number of combination of a, b firstly
for a in range(1, K + 1):
  for b in range(1, K + 1):
    cnt[gcd(a, b)] += 1
print(cnt)
for c in range(1, K + 1):
  for gcd_of_ab in cnt.keys():
    ans += gcd(gcd_of_ab, c) * cnt[gcd_of_ab]
print(ans)

"""
gcd(a,b,c)=gcd(gcd(a,b),c)

E.g.
a=b=c=3,
cnt=defaultdict(<class 'int'>, {1: 7, 2: 1, 3: 1})

If gcd(gcd_of_ab, c)=1, ans += 1 * 7
"""
