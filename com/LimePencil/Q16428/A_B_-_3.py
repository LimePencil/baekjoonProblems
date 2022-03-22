import sys

input = sys.stdin.readline

n,m = list(map(int,input().split(" ")))
if n%m >=0:
    print(n//m)
    print(n%m)
else:
    if m>0:
        print(n//m-1)
        print(n%m+m)
    else:
        print(n//m+1)
        print(n%m-m)