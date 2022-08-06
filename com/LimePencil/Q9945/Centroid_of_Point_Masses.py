import sys

input = sys.stdin.readline
cnt=0
while True:
    n = int(input())
    cnt+=1
    if n<0:
        break
    s=0
    s_x=0
    s_y=0
    for _ in range(n):
        x,y,m = list(map(int,input().split()))
        s+=m
        s_x+=m*x
        s_y+=m*y
    print(f"Case {cnt}: {s_x/s:.2f} {s_y/s:.2f}")
    input()