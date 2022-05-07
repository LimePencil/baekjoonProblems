import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr=[]
while len(arr)<n:
    arr+=list(map(int,input().split()))
ans =0
stack = deque()
start=1
end=1
for i in range(n):
    while stack and arr[stack[-1]] > arr[i]:
        last = stack.pop()
        if not stack:
            w=i
        else:
            w=i-stack[-1]-1
        x=w*arr[last]
        if x>ans:
            ans = x
            start=i-w+1
            end=i
        elif x==ans:
            if i-w+1<start:
                start=i-w+1
                end=i
    stack.append(i)
while stack:
    last = stack.pop()
    if not stack:
        w=n
    else:
        w=n-stack[-1]-1
    x=w*arr[last]
    if x>ans:
        ans = x
        start=n-w+1
        end=n
    elif x==ans:
        if n-w+1<start:
            start=n-w+1
            end=n
print(start,end,ans)