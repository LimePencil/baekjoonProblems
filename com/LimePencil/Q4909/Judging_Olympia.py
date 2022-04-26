import sys

input = sys.stdin.readline
while True:
    arr=list(map(int,input().split()))
    s=sum(arr)
    if s==0:
        break
    x=s-max(arr)-min(arr)
    print(x//4 if float.is_integer(x/4) else x/4)