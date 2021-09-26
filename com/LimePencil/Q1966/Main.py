import sys
from collections import deque

i = int(sys.stdin.readline())
for _ in range(i):
    n, m = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
    importance = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
    printer = deque(list(zip(importance,range(n))))
    importance.sort(reverse=True)
    counter = 0
    while True:
        a,b = printer.popleft()
        if(a == importance[0]):
            importance.pop(0)
            counter += 1
            if(b == m):
                print(str(counter))
                break
        else:
            printer.append((a,b))