import collections
import sys
from bisect import bisect_left
from collections import deque
n =  int(sys.stdin.readline().rstrip("\n"))
arr =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
longest = 0
stack =[]
dp = [0]*n
l = 0
for i in range(n):
    min_index = bisect_left(stack,arr[i])
    if min_index == l:
        stack.append(arr[i])
        l+=1
    else:
        stack[min_index] = arr[i]
    dp[i] = min_index
print(len(stack))
a = deque()
for i in range(n-1,-1,-1):
    if dp[i] == l-1:
        a.appendleft(arr[i])
        l-=1
print(*a)
