import sys
from collections import deque

n, k = list(map(int,sys.stdin.readline().strip("\n").split(" ")))

circle = deque(list(range(1, n+1)))
order = []
for i in range(n):
    for j in range(k):
        if(k-1 !=j):
            circle.append(circle.popleft())
        else:
            order.append(circle.popleft())

print("<" + ", ".join(str(x) for x in order) + ">")
    