H, W = map(int, input().split())

# append list per one row
# for _ in range(H):
#    aa = list(input())
#        a.append(aa)
A = [input() for _ in range(H)]

# extract the row if includes '#'
# E.g. ['##.#', '....', '##.#', '.#.#']-> ['##.#', '##.#', '.#.#']
A = list(filter(lambda a: any(x == '#' for x in a), A))

pprint(zip(*A))
# exchange column and row by zip(*A)
# E.g. ['##.#', '##.#', '.#.#'] -> ['##.', '###', '....', '###']
# extract the row if includes '#'
A = list(filter(lambda a: any(x == '#' for x in a), zip(*A)))

# exchange column and row by zip(*A)
for a in zip(*A):
    print(''.join(a))
