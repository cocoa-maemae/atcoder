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

The candidate points to cut is 13(L-1)
o|o|o|o|o|o|o|o|o|o|o|o|o

If the right side include as candidate points and would select 11 points in these,
o|o|o|o|o|o|o|o|o|o|o|o|o|
select cutting 10 points is possible, not 11 points. not satisfied problem condition.
o|o|o|o|o|o|o|o|o|o|ooo|
"""
