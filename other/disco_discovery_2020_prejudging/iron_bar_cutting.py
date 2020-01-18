N = int(input())
A = list(map(int, input().split()))
total = sum(A)
mid = total // 2 # seperation poin:
sum_left, sum_left2 = 0, 0
seperation_i = 0
"""
If A=[2,4,6,1,3,4], sum_left=12, sum_left2=6, seperation_i=2
"""
for i, l in enumerate(A[:-1]):
  sum_left += l
  if sum_left >= mid:
      seperation_i = i
      sum_left2 = sum_left - l
      break
"""
If A=[2,4,6,1,3,4], sum_right=8, sum_right2=14
"""
sum_right, sum_right2 = sum(A[seperation_i + 1:]), sum(A[seperation_i:])
print(min(abs(sum_right - sum_left), abs(sum_right2 - sum_left2)))
