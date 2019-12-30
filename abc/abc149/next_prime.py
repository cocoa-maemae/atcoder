import math
X = int(input())
def is_prime(X):
  i = 2
  while i <= math.sqrt(X):
    if X % i == 0:
      return False
    i += 1
  return True
while not is_prime(X):
  X += 1
print(X)
