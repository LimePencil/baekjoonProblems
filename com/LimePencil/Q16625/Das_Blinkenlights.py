import sys
import math

input = sys.stdin.readline
a,b,c = list(map(int,input().split()))
if math.lcm(a,b)<=c:
    print("yes")
else:
    print("no")