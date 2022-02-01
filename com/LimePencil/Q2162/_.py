from fnmatch import fnmatch
import sys

def checkIntersection(l1,l2):
    def ccw(px1,py1,px2,py2,px3,py3):
        x = (px2-px1)*(py3-py1)
        y= (px3-px1)*(py2-py1)
        if x>y:
            return 1
        elif x==y:
            return 0
        else:
            return -1
    x1,y1,x2,y2 = l1
    x3,y3,x4,y4 = l2   
    p123 = ccw(x1,y1,x2,y2,x3,y3)
    p124 = ccw(x1,y1,x2,y2,x4,y4)
    p341 = ccw(x3,y3,x4,y4,x1,y1)
    p342 = ccw(x3,y3,x4,y4,x2,y2)
    if p123*p124==0 and p341*p342==0:
        if min(x1, x2)<=max(x3,x4) and min(x3, x4)<=max(x1,x2) and min(y1, y2)<=max(y3,y4) and min(y3, y4)<=max(y1,y2):
            return True
        else:
            return False
    elif (p123*p124<0 and p341*p342<=0) or (p123*p124<=0 and p341*p342<0):
        return True
    else:
        return False

def union(p,a,b):
    a = find(p,a)
    b = find(p,b)
    if a< b:
        p[b] = a
    else:
        p[a] = b
def find(p,x):
    if p[x] != x:
        return find(p,p[x])
    return p[x]


n = int(sys.stdin.readline().rstrip("\n"))
lines = []
groups = 0
elements = [0]*n
max_connected = 0
members = list(range(n))
for i in range(n):
    lines.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
    for j in range(i):
        if checkIntersection(lines[i],lines[j]):
            union(members,i,j)
for i in range(n):
    if members[i] == i:
        groups +=1
    par = find(members,i)
    elements[par] +=1
    max_connected = max(max_connected,elements[par])
print(groups)
print(max_connected)