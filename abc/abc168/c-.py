import math
A, B, H, M = map(int, input().split())
th = (H * 60 + M) / 720 * 2 * math.pi
tm = M / 60 * 2 * math.pi
xh = A * math.cos(th)
yh = A * math.sin(th)
xm = B * math.cos(tm)
ym = B * math.sin(tm)
dx = xh - xm
dy = yh - ym
print(math.sqrt(dx * dx + dy * dy))


"""
See https://img.atcoder.jp/abc168/editorial.pdf
and https://www.youtube.com/watch?v=MXOSqPzsiqo&feature=youtu.be
Not need to use Cosine formula

Calculate angre of minutes and hour
theta m = M/60 * 2PI
theta h = (60*H+M)/720 * 2PI


"""
