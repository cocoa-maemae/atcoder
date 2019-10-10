# See https://img.atcoder.jp/agc038/editorial.pdf
H, W, A, B = map(int, input().split())
print("\n".join(["1" * A + "0" * (W - A)] * B + ["0" * A + "1" * (W - A)] * (H - B)))
