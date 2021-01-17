N, *S = map(str,open(0).read().split())
S = set(S)
for s in S:
  if "!" + s in S:
    print(s)
    exit()
print("satisfiable")
