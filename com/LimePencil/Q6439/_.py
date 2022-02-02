import sys
from itertools import combinations_with_replacement

# int(sys.stdin.readline().rstrip("\n"))

# list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))


def ccw(px1,py1,px2,py2,px3,py3):
    return (px2-px1)*(py3-py1)-(px3-px1)*(py2-py1)


t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    x1,y1,x2,y2 = arr[0:4]
    found = False
    ans = "F"
    points = [[min(arr[4],arr[6]),min(arr[5],arr[7])],[min(arr[4],arr[6]),max(arr[5],arr[7])],[max(arr[4],arr[6]),max(arr[5],arr[7])],[max(arr[4],arr[6]),min(arr[5],arr[7])]]
    for i in range(4):
        x3,y3 = points[i%4]
        x4,y4 = points[(i+1)%4]
        p123 = ccw(x1,y1,x2,y2,x3,y3)
        p124 = ccw(x1,y1,x2,y2,x4,y4)
        p341 = ccw(x3,y3,x4,y4,x1,y1)
        p342 = ccw(x3,y3,x4,y4,x2,y2)
        if p123*p124==0 and p341*p342==0:
            found = True
            if min(x1, x2)<=max(x3,x4) and min(x3, x4)<=max(x1,x2) and min(y1, y2)<=max(y3,y4) and min(y3, y4)<=max(y1,y2):
                ans = "T"
        if not found and p123*p124<=0 and p341*p342<=0:
            ans = "T"
            found = True
    if not found and (points[0][0]<x1<points[2][0] and points[0][1]<y1<points[2][1] and points[0][0]<x2<points[2][0] and points[0][1]<y2<points[2][1]):
        ans = "T"
    print(ans)

