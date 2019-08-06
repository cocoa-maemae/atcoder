from pprint import pprint
H, W = map(int, input().split())

# append list per one row
# for _ in range(h):
#    aa = list(input())
#        a.append(aa)
A = [input() for _ in range(H)]

# extract if all the row is '#'
A = list(filter(lambda a: any(x == '#' for x in a), A))

# exchange column and row by zip(*A)
# extract if all the row is '#'
A = list(filter(lambda a: any(x == '#' for x in a), zip(*A)))

# exchange column and row by zip(*A)
for a in zip(*A):
    print(''.join(a))
