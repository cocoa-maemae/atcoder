D, G = map(int, input().split())
PC = [0] + [list(map(int, input().split())) for _ in range(D)]
def dfs(i, g):
    # if reaches at the end, m + inifinity
    if i == 0:
        return 1e9
    # minimum problems count to solve
    m = min(g // (i * 100), PC[i][0])
    # score
    s = 100 * i * m 
    # bonus point
    if m == PC[i][0]:
        s += PC[i][1]
    # If sum is under g, call function again
    if s < g:
        # get minimums problems count to solve the rest sum
        m += dfs(i - 1, g - s)
    return min(m, dfs(i - 1, g))
print(dfs(D, G))
"""
E.g.
2 700
3 500
5 800

dfs(2, 700)->dfs(1, G - s)->dfs(0, G - s)
dfs(1, 700)->dfs(0, G - s)
"""
