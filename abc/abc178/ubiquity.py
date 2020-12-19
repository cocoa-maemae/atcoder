N=int(input())
MOD=10**9+7
ans=(pow(10,N,MOD)-pow(9,N,MOD)-pow(9,N,MOD)+pow(8,N,MOD))%MOD
print(ans)

"""
N 0~9
- includes 0 over 1
- includes 9 over 1

all the combination 10^N (0~9)
combination 0 dosen't exist 9^N (1~9)
combination 9 doesn't exist 9^N (0~8)
combination 0 and 9 don't exist 8^N (1~8)
the answer is 10^N-9^N-9^N+8^N

Write Venn diagram
--------
|       | 
| ----  |
| |  |  |
| -ans- |
|  |  | |
|  ---  |
--------

"""
