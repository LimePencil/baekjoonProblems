import sys
from bisect import bisect_left
n =  int(sys.stdin.readline().rstrip("\n"))
arr =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
longest = 0
stack =[]
l = 0
for i in range(n):
    min_index = bisect_left(stack,arr[i])
    if min_index == l:
        stack.append(arr[i])
        l+=1
    else:
        stack[min_index] = arr[i]
print(l)
