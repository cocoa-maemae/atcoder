import sys
"""
click Ctrl+D finally
"""
"""
*PS type is list. 
E.g. 
['1', 'WA', '1', 'AC', '2', 'WA', '2', 'AC', '2', 'WA']
"""
N, M = map(int, input().split())
PS = sys.stdin.read().strip().split()
ac, wa = [0] * N, [0] * N # index means p
"""
convert list to dict by using zip
E.g.
['1', 'WA', '1', 'AC', '2', 'WA', '2', 'AC', '2', 'WA']
->[('1', 'WA'),('1','AC')....]
"""
for p, s in zip(*[iter(PS)] * 2):
    p = int(p) - 1 # index starts from 0
    if s == "AC":
        ac[p] = 1
    elif s == "WA" and ac[p] == 0: # if WA is 0 at the p try, count WA.
        wa[p] += 1
"""
If *PA=['1', 'WA', '1', 'AC', '2', 'WA', '2', 'AC', '2', 'WA'],
ac=[1,1]
wa=[1,1]
"""
penalties = sum([w if a > 0 else 0 for a, w in zip(ac, wa)])
print(sum(ac), penalties)


"""
Similar like
C - Peaks
"""
