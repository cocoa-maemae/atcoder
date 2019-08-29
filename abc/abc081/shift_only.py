import math

N = int(input())
A = list(map(int, input().split()))
ans = float("inf")
for a in A:
    # If target number is 8(=0b1000), divided count by 2 is 3. 
    # It is same as the number of 0 of binary expression
    divi_cnt_by_2 = len(bin(a)) - bin(a).rfind("1") - 1
    ans = min(ans, divi_cnt_by_2)
print(round(ans))
