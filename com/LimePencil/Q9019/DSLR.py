import sys
from collections import deque

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    start, target = map(int,sys.stdin.readline().rstrip("\n").split(" "))
    q = deque()
    q.append((start,""))
    v = [False]*10000
    while q:
        num, c = q.popleft()
        v[num] = True
        num2 = (2*num)%10000
        if num == target:
            print(c)
            break
        if not v[num2]: 
            if num2 == target:
                print(c+"D")
                break
            q.append((num2,c+"D"))
            v[num2] = True
        num2 =num - 1 if num != 0 else 9999
        if not v[num2]:
            if num2 == target:
                print(c+"S")
                break
            q.append((num2,c+"S"))
            v[num2] = True
        num2= int(num % 1000 * 10 + num / 1000)
        if not v[num2]:
            if num2 == target:
                print(c+"L")
                break
            q.append((num2,c+"L"))
            v[num2] = True
        num2 = int(num % 10 * 1000 + num // 10)
        if not v[num2]:
            if num2 == target:
                print(c+"R")
                break
            q.append((num2,c+"R"))
            v[num2] = True