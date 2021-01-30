import math
A, B, H, M = map(int, input().split())
th = (H * 60 + M) / 720 * 2 * math.pi
tm = M / 60 * 2 * math.pi
xh, yh = A * math.cos(th), A * math.sin(th)
xm, ym = B * math.cos(tm), B * math.sin(tm)
dx = xh - xm
dy = yh - ym
print(math.sqrt(dx * dx + dy * dy))


"""
See https://www.youtube.com/watch?v=MXOSqPzsiqo&feature=youtu.be
Not need to use Cosine formula

Calculate angle of minutes and hour(2PI=360)
# Regarding h, 1circle=12h=720min
# theta h=H*60/720 is mistake, because hour hand moves 1 hour
# with set of hour and min(1h+60min)
theta h = (H*60+M)/720*2PI

# Regarding m, 1circle=60min
theta m = M/60*2PI
See https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1391868678

Next use sin and cos.
If the answer is L
A/L=cos(theta)->A=L*cos(theta)
B/L=sin(theta)->B=L*sin(theta)

"""
