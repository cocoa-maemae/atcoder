import sys
from collections import Counter
N = int(input())
S = (str(x) for x in sys.stdin.read().split())
cnt = Counter(s for s in S)
max_cnt = max(cnt.values())
keys = [k for k, v in cnt.items() if v == max_cnt]
print("\n".join(sorted(keys)))
