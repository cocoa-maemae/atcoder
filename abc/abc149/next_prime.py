import math
X = int(input())
def is_prime(X):
  n = 2
  while n <= math.sqrt(X):
    if X % n == 0:
      return False
    n += 1
  return True
while not is_prime(X):
  X += 1
print(X)
