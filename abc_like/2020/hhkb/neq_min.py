N = int(input())
P = list(map(int, input().split()))
check = [False] * 200001
ans = 0
for i in range(N):
  check[P[i]] = True
  if ans == P[i]:
    while check[ans]: # if check[ans]==False, break loop
      ans += 1
  print(ans)

"""
4
1 1 0 2

P[0]=1,check[1]=True,print(0),ans=0
P[1]=1,check[1]=True,print(0),ans=0
P[2]=0,check[0]=True,ans==P[2],ans=1

"""
