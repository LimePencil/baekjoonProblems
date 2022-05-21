import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n,d=list(map(int,input().split()))
    cnt=0
    for _ in range(n):
        v,f,c= list(map(int,input().split()))
        if d/v*c<=f:
            cnt+=1
    print(cnt)