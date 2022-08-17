import sys

input = sys.stdin.readline
while True:
    a,b,c=list(map(int,input().split()))
    if a==b==c==0:
        break
    t=round(a*3600/b-a*3600/c)
    print(f"{t//3600}:{t%3600//60:02}:{t%60:02}")