def sum(n):
  return (n * (n + 1)) // 2
N = int(input())
fizz_cnt = N // 3
buzz_cnt = N // 5
fizzbuzz_cnt = N // 15
print(sum(N) - 3 * sum(fizz_cnt) - 5 * sum(buzz_cnt) + 15 * sum(fizzbuzz_cnt))


"""
sum of all - sum of 3 multiple - sum of 5 multiple + sum of 15 multiple

----------
     ------
-----| 5m |
|   15m   |
| 3m |
|    |-----
-----
----------

"""
