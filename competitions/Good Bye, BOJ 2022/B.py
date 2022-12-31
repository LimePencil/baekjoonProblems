import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()
n=int(input())
arr=sorted(list(map(int,input().split())))

if len(arr)>3:
    s=sum(arr[1:])
    m=(s+arr[0])/n
    for i in range(1,n):
        m=max(m,min((s-arr[i])/(n-2),arr[i]))
    print(m)
elif len(arr)==3:
    print(max(arr[1],(arr[0]+arr[1]+arr[2])/3))
else:
    print((arr[0]+arr[-1])/2)