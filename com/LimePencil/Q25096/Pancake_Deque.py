import math
import sys
from collections import deque

input = sys.stdin.readline
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    q=deque(arr)
    m=0
    while q:
        if q[0]<=q[-1]:
            a=q.popleft()
            if a>=m:
                m=a
                ans+=1
        else:
            a=q.pop()
            if a>=m:
                m=a
                ans+=1
    print("Case #{}: {}".format(t+1,ans))