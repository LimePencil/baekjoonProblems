import sys

input=sys.stdin.readline

def XOR(n) :
    if n%4 == 0:
        return n
    if n%4 == 1:
        return 1
    if n%4== 2:
        return n+1
    return 0
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(XOR(b)^XOR(a-1))