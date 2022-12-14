import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    a,b,c = list(map(int,input().split()))
    print("Data set:",a,b,c)
    for _ in range(c):
        if a>b:
            a//=2
        else:
            b//=2
    if b>a:
        a,b=b,a
    print(a,b)
    print()
