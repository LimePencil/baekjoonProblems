import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()
n,point,p = list(map(int,input().split()))
arr=[]
if n >0:
    arr=list(map(int,input().split()))
idx=bisect.bisect_right(arr[::-1],point)
idx=n+1-idx
print(-1 if (len(arr)==p and arr[-1]==point) or idx>p else idx)