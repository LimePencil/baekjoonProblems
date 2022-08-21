import sys

input = sys.stdin.readline
a,b = list(map(float,input().split()))
n = int(input())
for _ in range(n):
    w,c=input().split()
    w=float(w)
    if c=="A":
        print(w*b/a)
    else:
        print(w*a/b)