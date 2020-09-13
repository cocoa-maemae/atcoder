X, K, D = map(int, input().split())
X = abs(X)
cnt_before_0 = X // D
if cnt_before_0 >= K:
  print(X - D * K)
  exit()
if (cnt_before_0 % 2) ^ (K % 2) == 0: # same as (K-cnt_before_0) % 2 == 0 but slower.
  print(X - D * cnt_before_0)
else:
  print(abs(X - D * cnt_before_0 - D))

"""
Get absolute value of X initially, and then like the below,
-----0-----------------X---

Case 1.
When repeat X-D in K times.
If end before round-trip of 0, it does mean X-D*K>=0 -> X>=D*K -> X//D>=K,
the answer is X-D*K.
But D*K is overflow in C or C++. 
-----0-----------------X--
-----0---------(X-D)------
-----0---(X-D)------------


Case 2.
When repeat X-D in K times.
If not end before 0, set cnt_before_0=X//D
If K-cnt_before_0 is odd, answer is X-D*cnt_before_0-D

-------0---------------X-
-------0------(X-D)------
-------0-(X-D)----------- moved cnt_before_0 count
-(X-D)-0----------------- 1
-------0-(X-D)----------- 2
-(X-D)-0----------------- 3

If K-cnt_before_0 is odd, answer is X-D*cnt_before_0-D

-------0---------------X-
-------0------(X-D)------
-------0-(X-D)----------- moved cnt_before_0 count
-(X-D)-0----------------- 1
-------0-(X-D)----------- 2 
-(X-D)-0----------------- 3
-------0-(X-D)----------- 4
"""
