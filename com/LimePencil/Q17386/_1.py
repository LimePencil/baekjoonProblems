import sys

def ccw(px1,py1,px2,py2,px3,py3):
    return (px2-px1)*(py3-py1)-(px3-px1)*(py2-py1)

x1,y1,x2,y2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
x3,y3,x4,y4 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

p123 = ccw(x1,y1,x2,y2,x3,y3)
p124 = ccw(x1,y1,x2,y2,x4,y4)
p341 = ccw(x3,y3,x4,y4,x1,y1)
p342 = ccw(x3,y3,x4,y4,x2,y2)
print("1" if p123*p124<=0 and p341*p342<=0 else "0")
