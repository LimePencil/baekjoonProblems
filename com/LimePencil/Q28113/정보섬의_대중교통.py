import sys

input = lambda: sys.stdin.readline().rstrip()
n,a,b = list(map(int,input().split()))
if b>=n:
    if b<a:
        print("Subway")
    elif b>a:
        print("Bus")
    else:
        print("Anything")
else:
    print("Bus")