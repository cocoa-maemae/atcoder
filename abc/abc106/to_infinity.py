S = input()
K = int(input())
   
for c in S:
    # neglect except for 1, because other numbers are infinite.
    if c == '1':
        # if the distance is 1, 1 is the answer.
        if K == 1:
            print(1)
            break
        # if the distance is not 1, 1 minus from distance
        K -= 1
        continue
    print(c)
    break
