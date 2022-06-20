import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
if n>=6:
    print("Love is open door")
else:
    for _ in range(1,n):
        if m==1:
            m=0
        else:
            m=1
        print(m)