import sys

input = sys.stdin.readline
while True:
    d,h,v=input().split()
    d=float(d)
    h=int(h)
    v=int(v)
    if d==h==v==0:
        break
    print(f"Horizontal DPI: {h/(16*d/(337)**0.5):.2f}")
    print(f"Vertical DPI: {v/(16*d/(337)**0.5)*(16/9):.2f}")