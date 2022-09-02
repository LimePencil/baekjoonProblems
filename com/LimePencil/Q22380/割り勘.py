import sys

input = sys.stdin.readline
while True:
    n,m = list(map(int,input().split()))
    if n==m==0:
        break
    arr=list(map(int,input().split()))
    money=0
    for a in arr:
        money+=min(m//n,a)
    print(money)