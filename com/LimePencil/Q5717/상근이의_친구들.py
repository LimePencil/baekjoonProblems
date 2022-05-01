import sys

input = sys.stdin.readline
while True:
    s=sum(map(int,input().split()))
    if s==0:
        break
    else:
        print(s)