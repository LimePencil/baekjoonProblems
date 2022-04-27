import sys
import math

input = sys.stdin.readline
for t in range(1,int(input())+1):
    b,w=list(map(float,input().split()))
    b=int(b)
    balloon=sum([float(input())**3*math.pi*4/3000 for _ in range(b)])
    print("Data Set {}:".format(t))
    if balloon>=w:
        print("Yes")
    else:
        print("No")
    print()