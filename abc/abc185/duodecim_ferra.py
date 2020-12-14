from math import factorial
def combination(n, r):
  return factorial(n) // (factorial(n - r) * factorial(r))
L = int(input())
print(combination(L-1, 11))

"""
The answer is
L-12+11C11=L-1C11

E.g.
L=13

The candidate points to cut is 12(L-1)
o|o|o|o|o|o|o|o|o|o|o|o|o
"""
