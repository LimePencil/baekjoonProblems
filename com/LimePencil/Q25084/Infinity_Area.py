import math
import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    r,a,b=list(map(int,input().split()))
    ans=0
    a_done=False
    while r !=0:
        ans+=r*r*math.pi
        if not a_done:
            r*=a
            a_done=True
        else:
            r//=b
            a_done=False

    print("Case #{}: {}".format(t,ans))