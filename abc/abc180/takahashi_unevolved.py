X, Y, A, B = map(int, input().split())
experience = 0
while A * X <= X + B and A * X < Y:
  X *= A
  experience += 1
experience += (Y - X - 1) // B
print(experience)


"""
If x*A<=x+B, use A
If x*B<=x+A, use B

If go to Kakomon Gym firstly and then go to AtCoder Gym, X->XA->XA+B
If go to AtCoder Gym firstly and then go to Kakomon Gym, X->X+B->XA+BA

"""
