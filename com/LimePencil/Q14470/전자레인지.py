import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t = 0
if a<0:
    t+=c*abs(a)+d
    a = 0
if a>=0:
    t+=e*(b-a)
print(t)