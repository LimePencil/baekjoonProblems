import sys

input = sys.stdin.readline
while True:
    a,b=list(map(int,input().split()))
    if a==0 and b==0:
        break
    a-=b
    print(0 if a<3 else (a-3)//2 if a%2==1 else a//2,int(a%2==1 and a>=3))