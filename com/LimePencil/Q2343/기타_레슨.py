import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
lectures=list(map(int,input().split()))
s=max(lectures)
e=sum(lectures)
while s<=e:
    mid=(s+e)//2
    blueray_used=1
    space=0
    for l in lectures:
        if space+l<=mid:
            space+=l
        else:
            space=l
            blueray_used+=1
    if blueray_used>m:
        s=mid+1
    else:
        e=mid-1
print(s)