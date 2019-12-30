D, G = map(int, input().split())
PC = [0] + [list(map(int, input().split())) for _ in range(D)]
def dfs(i, g):
    # if reaches at the end, m + inifinity
    if i == 0:
        return 1e9
    # the minimum problem count which can solve
    # i * 100 means the current score per one problem
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

# check from 5, 800
->dfs(2, 700): i=2, g=700, m=3, s=600, if(600<700)
    m+=dfs(2-1, 700-200*3)=3+1=4
    ->dfs(1, 100): i=1, g=100, m=1, s=100, if(100<100)
        return min(1, dfs(1-1, 100))=1
    return min(4, dfs(2-1, 700))=min(4, 3)=3 # 4 is the minumum count when i=2
    ->dfs(1, 700): i=1, g=700, m=3, s=300, if(300<700)
        m+=dfs(1-1, 700-300)=3+0=3
        return (3, dfs(1-1, 700))=3 # 3 is the minimum count when i=1 
"""
