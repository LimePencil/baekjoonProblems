import sys
from collections import deque

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
target = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
d = deque(range(1,n+1))
count= 0
for i in target:
    if d.index(i) < len(d)/2:
        while(d[0] != i):
            d.append(d.popleft())
            count +=1
    else:
        while(d[0] != i):
            d.appendleft(d.pop())
            count +=1
    d.popleft()
print(count)
