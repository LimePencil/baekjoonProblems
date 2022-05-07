import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr=list(map(int,input().split()))
ans =0
stack = deque()
for i in range(n):
    while stack and arr[stack[-1]] > arr[i]:
        last = stack.pop()
        if not stack:
            w=i
        else:
            w=i-stack[-1]-1
        ans = max(ans,w*arr[last])
    stack.append(i)
while stack:
    last = stack.pop()
    if not stack:
        w=n
    else:
        w=n-stack[-1]-1
    ans = max(ans,w*arr[last])
print(ans)