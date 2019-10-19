A, B = map(int, input().split())

def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
      while n % i == 0:   #iで割り切れれば、iはnの素因数
          n /= i
          table.append(i)
      i += 1
  if n > 1:
      table.append(n)
  return table

x = set(prime_decomposition(A))
y = set(prime_decomposition(B))
print(len(x & y) + 1)
