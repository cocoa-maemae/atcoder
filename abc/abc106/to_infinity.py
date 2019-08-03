S = input()
K = int(input())
   
for c in S:
    if c == '1':
        if K == 1:
            print(1)
            break
        K -= 1
        continue
    print(c)
    break
