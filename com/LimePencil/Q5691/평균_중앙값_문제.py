import sys

input = lambda: sys.stdin.readline().rstrip()
while True:
    a,b=list(map(int,input().split()))
    if a==b==0:
        break
    print(2*a-b)