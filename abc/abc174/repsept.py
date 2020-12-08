K = int(input())
if K % 2 == 0 or K % 5 == 0:
  print(-1)
  exit()
i, ai = 0, 0
while True:
  ai = (ai * 10 + 7) % K
  i += 1
  if ai == 0:
    print(i)


"""
Given array 7,77,777...
set as ai

ai= { 
  7 mod K (i = 1)
  (10 * ai−1 + 7) mod K (i ≥ 2)
}


And K and 10 must be coprime, 
so if K%2==0 or K%5==0, answer is -1
"""
