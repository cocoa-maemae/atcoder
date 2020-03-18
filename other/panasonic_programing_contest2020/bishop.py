H, W = map(int, input().split())
# corner case
if H == 1 or W == 1:
  print(1)
  exit()
"""
If the number of cells is even, the answer is half of cell.
If the number of cells is odd, the answer is (cell count + 1) // 2
"""
print((H * W + 1) // 2)
