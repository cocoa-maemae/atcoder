a, b, x = map(int, input().split())
import math
if a * a * b >= x * 2:
    c = x * 2 / (b * a)
    print(math.degrees(math.atan(b / c)))
else:
    d = 2 * (b - x / a / a)
    print(math.degrees(math.atan(d / a)))
