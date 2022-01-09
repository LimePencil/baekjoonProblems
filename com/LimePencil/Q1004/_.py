import sys

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    x1, y1, x2,y2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    count = 0
    n = int(sys.stdin.readline().rstrip("\n"))
    for _ in range(n):
        a,b,r = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        d1 = (((x1-a)**2+(y1-b)**2)**0.5)<r
        d2 = ((x2-a)**2+(y2-b)**2)**0.5<r
        if d1 ^ d2:
            count+=1
    print(count)