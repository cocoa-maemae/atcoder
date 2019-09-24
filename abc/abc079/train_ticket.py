A, B, C, D = input()
o = ["+", "-"]
for i in range(2):
    for j in range(2):
        for k in range(2):
            s = A + o[i]  + B + o[j] + C + o[k] + D
            if eval(s) == 7:
                print(s + "=7")
                exit()
