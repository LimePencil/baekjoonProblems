import sys
from collections import deque

s = sys.stdin.readline().rstrip("\n")
bomb = sys.stdin.readline().rstrip("\n")

stack = deque()

for k,c in enumerate(s):
    if c == bomb[-1]:
        found = True
        for i in range(len(bomb)-1):
            if len(stack)+1<len(bomb) or stack[-1-i] != bomb[len(bomb)-i-2]:
                found = False
                stack.append(c)
                break      
        if found:
            for i in range(len(bomb)-1):
                stack.pop()
    else:
        stack.append(c)
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))