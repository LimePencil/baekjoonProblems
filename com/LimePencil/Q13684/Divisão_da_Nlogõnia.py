import sys

input = sys.stdin.readline
while True:
    k=int(input())
    if k==0:
        break
    n,m=list(map(int,input().split()))
    for _ in range(k):
        x,y=list(map(int,input().split()))
        if x==n or y==m:
            print("divisa")
        elif x>n and y>m:
            print("NE")
        elif x<n and y>m:
            print("NO")
        elif x<n and y<m:
            print("SO")
        else:
            print("SE")