N, K = map(int, input().split())
r = N % K 
print(min(r, abs(r - K)))

"""
Similar with ABC175 C

E.g.
If N=100, K=7
100-93-86-79-72-65-58-51-44-37-30-23-16-9-2-5-2-5-2-5-2.....
- 100 % 7 = 2
- 2 - 7 = 5

If N=7, K=4
7-3-1-3-1-3...
- 7 % 4 = 3
- 3 - 4 = 1
"""
