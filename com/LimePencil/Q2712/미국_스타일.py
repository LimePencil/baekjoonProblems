import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a,b=input().split()
    if b=="kg":
        print("{:.4f} lb".format(float(a)*2.2046))
    elif b=="lb":
        print("{:.4f} kg".format(float(a)*0.4536))
    elif b=="l":
        print("{:.4f} g".format(float(a)*0.2642))
    else:
        print("{:.4f} l".format(float(a)*3.7854))