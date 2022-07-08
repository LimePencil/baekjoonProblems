import sys

input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    if n%6==0:
        print((n-1)*(n-2)*(n-3))
    elif n%2==0:
        print(n*(n-1)*(n-3))
    else:
        print(n*(n-1)*(n-2))