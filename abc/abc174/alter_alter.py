N = int(input())
c = input()
red_cnt = c.count("R")
ans = c[:red_cnt].count("W")
print(ans)

"""
The left side of white is all red.

E.g.
RRRRRRW
RRRWWWW

If C is like
WRRWRWWRR
have to change like
RRRWWWWWW

In this case,
R->R*2
R->W*3 want to make R count 0
W->R*1 want to make W count 0
W->W*3

Consider dividor from the left
Case1
WRRWRWWRR
WWWWWWWWW
R->W*5
W->R*0

Case2
WRRWRWWRR
RWWWWWWWW
R->W*5
W->R*1

Case3
WRRWRWWRR
RRWWWWWWW
R->W*4
W->R*1

Case4
WRRWRWWRR
RRRWWWWWW
R->W*3
W->R*1
"""
