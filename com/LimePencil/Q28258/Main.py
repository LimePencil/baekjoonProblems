import sys
from collections import deque

n = int(sys.stdin.readline().strip("\n"))
queue = deque()
for _ in range(n):
    order = sys.stdin.readline().strip("\n").split(" ")
    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "front":
        print(queue[0] if  len(queue) != 0 else -1)
    elif order[0] == "back":
        print(queue[-1] if len(queue) != 0 else -1)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif order[0] == "pop":
        print(queue.popleft() if len(queue) != 0 else -1)

