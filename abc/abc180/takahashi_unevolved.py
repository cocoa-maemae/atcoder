X, Y, A, B = map(int, input().split())
experience, strength = 0, X
while strength * A <= strength + B and strength * A < Y:
  X *= A
  experience += 1
experience += (Y - X - 1) // B # add rest experience if B is added
print(experience)

"""
To increase experience, consider use A or B,
If x*A<=x+B, use A
If x*B<=x+A, use B

If go to Kakomon Gym firstly and then go to AtCoder Gym, X->XA->XA+B
If go to AtCoder Gym firstly and then go to Kakomon Gym, X->X+B->XA+BA
"""
