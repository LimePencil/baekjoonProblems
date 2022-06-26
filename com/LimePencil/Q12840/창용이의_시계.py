from datetime import datetime, timedelta
import sys

input = sys.stdin.readline
h,m,s = list(map(int,input().split()))
t=datetime(2000,1,1,h,m,s)
for _ in range(int(input())):
    arr=list(map(int,input().split()))
    if arr[0]==1:
        t+=timedelta(seconds=arr[1])
    elif arr[0]==2:
        t-=timedelta(seconds=arr[1])
    else:
        print(t.hour,t.minute,t.second)