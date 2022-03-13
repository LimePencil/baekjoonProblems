import sys
from collections import deque

input = sys.stdin.readline
while True:
    arr = list(map(int,input().split(" ")))
    if arr == [0]:
        break
    ans =0
    stack = deque()
    for i in range(arr[0]):
        while stack and arr[stack[-1]+1] > arr[i+1]:
            last = stack.pop()
            if not stack:
                w=i
            else:
                w=i-stack[-1]-1
            ans = max(ans,w*arr[last+1])
        stack.append(i)
    while stack:
        last = stack.pop()
        if not stack:
            w=arr[0]
        else:
            w=arr[0]-stack[-1]-1
        ans = max(ans,w*arr[last+1])
    print(ans)