X, Y, A, B = map(int, input().split())
a_cnt = 0
while A * X <= X + B and A * X < Y:
  X *= A
  a_cnt += 1
b_cnt = (Y - X - 1) // B
print(a_cnt + b_cnt)


"""
If x*A<=x+B, use A
If x*B<=x+A, use B

If go to Kakomon Gym firstly and then go to AtCoder Gym, X->XA->XA+B
If go to AtCoder Gym firstly and then go to Kakomon Gym, X->X+B->XA+BA

"""
