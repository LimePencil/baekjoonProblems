import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
print(a+b+c+d+e+f-min(a,b,c,d)-min(e,f))