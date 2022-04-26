import sys

input = sys.stdin.readline
while True:
    a,b,c=list(map(int,input().split()))
    if a==0 and b==0 and c==0:
        break
    print((c-a)//b+1 if (c-a)%b==0 and (c-a)//b>=0 else "X")