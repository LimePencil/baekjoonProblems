import math
import sys

input = sys.stdin.readline
a1,p1 = list(map(int,input().split(" ")))
a2, p2 = list(map(int,input().split(" ")))
a2 = a2**2*math.pi
if a1/p1 > a2/p2:
    print("Slice of pizza")
else:
    print("Whole pizza")