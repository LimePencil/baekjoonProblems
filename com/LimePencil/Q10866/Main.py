from collections import deque
import sys

n = int(sys.stdin.readline())
deq = deque()
for _ in range(n):
    command = sys.stdin.readline().strip("\n").split(" ")
    order = command[0]
    if order == "push_back":
        deq.append(int(command[1]))
    elif order == "push_front":
        deq.appendleft(int(command[1]))
    elif order == "pop_front":
        if(len(deq) != 0):
            print(str(deq.popleft()))
        else:
            print("-1")
    elif order == "pop_back":
        if(len(deq) != 0):
            print(str(deq.pop()))
        else:
            print("-1")
    elif order == "size":
        print(str(len(deq)))
    elif order == "front":
        if(len(deq) != 0):
            print(str(deq[0]))
        else:
            print("-1")
    elif order == "back":
        if(len(deq) != 0):
            print(str(deq[-1]))
        else:
            print("-1")
    elif order == "empty":
        print("1" if len(deq) ==0 else "0")