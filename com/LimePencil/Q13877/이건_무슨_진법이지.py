import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    a,b = input().split()
    b=str(int(b))
    if "9" in b or "8" in b:
        print(a,0,b,int(b,16))
    else:
        print(a,int(b,8),b,int(b,16))