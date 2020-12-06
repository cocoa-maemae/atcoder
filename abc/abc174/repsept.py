K = int(input())
if K % 2 == 0 or K % 5 == 0:
  print(-1)
  exit()
i, ai = 0, 0
while True:
  ai = (ai * 10 + 7) % K
  i += i
  if ai == 0:
    print(ai)
    exit()


"""
Given array 7,77,777...

ai= { 
7 mod K ( i = 1)
10 * ai−1 + 7 mod K ( i ≥ 2)
}

"""
