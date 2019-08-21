from pprint import pprint
N, K = map(int, input().split())
x = list(map(int, input().split()))

# mapping [X0...] [Xk-1...] by zip
#for a, b in zip(x, x[K-1:]):
#    print(a, b)
# the answer is the minimum number of Xi+k−1 − Xi + min(|Xi|,|Xi+k−1|) 
ans = min(b - a + min(abs(a), abs(b)) for a, b in zip(x, x[K-1:]))
print(ans)
