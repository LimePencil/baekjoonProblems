import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
ans =0
stack = deque()
start=1
end=1
for i in range(n):
    t=0
    while stack and arr[stack[-1][0]] > arr[i]:
        last,te = stack.pop()
        if not stack:
            w=i
        else:
            w=i-stack[-1][0]-1
        t+=te
        x=t*arr[last]
        if x>ans:
            ans = x
            start=i-w+1
            end=i
    t+=arr[i]
    stack.append((i,t))
t=0
while stack:
    last,te = stack.pop()
    if not stack:
        w=n
    else:
        w=n-stack[-1][0]-1
    t+=te
    x=t*arr[last]
    if x>ans:
        ans = x
        start=n-w+1
        end=n
print(ans)
print(start,end)