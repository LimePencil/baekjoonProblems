import sys

def ccw(px1,py1,px2,py2,px3,py3):
    return (px2-px1)*(py3-py1)-(px3-px1)*(py2-py1)

n = int(sys.stdin.readline().strip("\n").strip(" "))
arr = list(map(int,sys.stdin.readline().strip("\n").strip(" ").split(" ")))
k = int(sys.stdin.readline().strip("\n").strip(" "))
found = False
if n ==1 and arr[0] == k:
    found = True
    print("T")
for i in range(1,n):

    x1 = i
    y1 = arr[i-1]
    x2 = i+1
    y2 = arr[i]
    x3 = i
    y3 = i*k
    x4 = i+1
    y4 = (i+1)*k
    p123 = ccw(x1,y1,x2,y2,x3,y3)
    p124 = ccw(x1,y1,x2,y2,x4,y4)
    p341 = ccw(x3,y3,x4,y4,x1,y1)
    p342 = ccw(x3,y3,x4,y4,x2,y2)
    if p123*p124==0 and p341*p342==0:
        found = True
        if min(x1, x2)<=max(x3,x4) and min(x3, x4)<=max(x1,x2) and min(y1, y2)<=max(y3,y4) and min(y3, y4)<=max(y1,y2):
            print("T")
            break
    if not found and p123*p124<=0 and p341*p342<=0:
        found = True
        print("T")
        break
if not found:
    print("F")