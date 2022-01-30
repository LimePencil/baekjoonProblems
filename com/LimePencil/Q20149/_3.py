import sys

def ccw(px1,py1,px2,py2,px3,py3):
    return (px2-px1)*(py3-py1)-(px3-px1)*(py2-py1)
def intersection(px1,py1,px2,py2,px3,py3,px4,py4):
    PX = (px1*py2 - py1*px2)*(px3-px4) - (px1-px2)*(px3*py4 - py3*px4)
    PY = (px1*py2 - py1*px2)*(py3-py4) - (py1-py2)*(px3*py4 - py3*px4)
    P = (px1-px2)*(py3-py4) - (py1-py2)*(px3-px4)
    if P==0:
        if px1>px2 or px1 == px2 and py1>py2:
            px1,px2 = px2,px1
            py1,py2 = py2,py1
        if px3>px4 or px3 == px4 and py3>py4:
            px3,px4 = px4,px3
            py3,py4 = py4,py3
        if px2 == px3 and py2 == py3:
            print(str(px2) + " " + str(py2))
        elif px1 == px4 and py1 == py4:
            print(str(px1) + " " + str(py1))
    else:
        f = PX/P
        s= PY/P
        if float.is_integer(f):
            f = int(f)
        if float.is_integer(s):
            s = int(s)
        print(str(f) + " "+ str(s) )

x1,y1,x2,y2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
x3,y3,x4,y4 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

p123 = ccw(x1,y1,x2,y2,x3,y3)
p124 = ccw(x1,y1,x2,y2,x4,y4)
p341 = ccw(x3,y3,x4,y4,x1,y1)
p342 = ccw(x3,y3,x4,y4,x2,y2)
ans = 0
if p123*p124==0 and p341*p342==0:
    if min(x1, x2)<=max(x3,x4) and min(x3, x4)<=max(x1,x2) and min(y1, y2)<=max(y3,y4) and min(y3, y4)<=max(y1,y2):
        print("1")
        intersection(x1,y1,x2,y2,x3,y3,x4,y4)
    else:
        print("0")
elif (p123*p124<0 and p341*p342<=0) or (p123*p124<=0 and p341*p342<0):
    print("1")
    intersection(x1,y1,x2,y2,x3,y3,x4,y4)
else:
    print("0")