import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
if m<n:
    m+=360
a=m-n
b=a-360
print(a if abs(a)<=abs(b) else b)