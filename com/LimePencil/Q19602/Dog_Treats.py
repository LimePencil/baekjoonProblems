import sys

input = sys.stdin.readline
s = int(input())
m = int(input())
l = int(input())
if s+m*2+l*3>=10:
    print("happy")
else:
    print("sad")