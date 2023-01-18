import sys
import math

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    a,p1 = list(map(int,input().split()))
    r,p2 = list(map(int,input().split()))

    print("Slice of pizza" if a/p1>r**2*math.pi/p2 else "Whole pizza")
