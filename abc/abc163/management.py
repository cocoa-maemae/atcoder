N = int(input())
A = list(map(int, input().split()))
subordinate_cnt = [0] * N
for boss_num in A:
  subordinate_cnt[boss_num - 1] += 1
print("\n".join(map(str, subordinate_cnt)))

"""
map(str, list) converts int element of list to str
"""
