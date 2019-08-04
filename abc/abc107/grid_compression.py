H, W = map(int, input().split())
A = [input() for _ in range(H)]
A = list(filter(lambda a: any(x == '#' for x in a), A))
A = list(filter(lambda a: any(x == '#' for x in a), zip(*A)))
for a in zip(*A):
    print(''.join(a))
