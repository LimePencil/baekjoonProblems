import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
ans =0
stack = deque()
for i in range(n):
    t=0
    while stack and arr[stack[-1][0]] > arr[i]:
        last,te = stack.pop()
        t+=te
        x=t*arr[last]
        ans = max(ans,x)
    t+=arr[i]
    stack.append((i,t))
t=0
while stack:
    last,te = stack.pop()
    t+=te
    x=t*arr[last]
    ans = max(ans,x)
print(ans)