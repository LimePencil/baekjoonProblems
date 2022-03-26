import sys

input = sys.stdin.readline
x,l,r = list(map(int,input().split()))
if x<l:
    print(l)
elif x>r:
    print(r)
else:
    print(x)