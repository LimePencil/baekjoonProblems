import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    n=bin(n)[2:]
    pos=[]
    for i in range(len(n)):
        if n[len(n)-i-1]=="1":
            pos.append(i)
    print(*pos)