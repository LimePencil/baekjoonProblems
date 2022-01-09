import sys
import math

x1, y1 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
x2, y2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
x3, y3 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
rad = (x1*y2+y1*x3+x2*y3)-(x3*y2+y3*x1+x2*y1)
if rad ==0:
    print("0")
elif rad > 0:
    print("1")
else:
    print("-1")