import sys
import math
x1, y1, r1, x2, y2, r2 = list(map(float,sys.stdin.readline().rstrip("\n").split(" ")))
d = ((x1-x2)**2 + (y1-y2)**2)**0.5
if r2> r1:
    r1,r2 = r2,r1

if d >=r1+r2:
    print("0.000")
elif r1 >= d + r2:
    print(round(math.pi*r2*r2,3))
else:
    p1 = r1*r1*math.acos((d*d + r1*r1 - r2*r2)/(2*d*r1))
    p2 = r2*r2*math.acos((d*d + r2*r2 - r1*r1)/(2*d*r2))
    p3 = 0.5*math.sqrt((-d+r1+r2)*(d+r1-r2)*(d-r1+r2)*(d+r1+r2))
    intersectionArea = p1 + p2 - p3
    print(round(intersectionArea,3))