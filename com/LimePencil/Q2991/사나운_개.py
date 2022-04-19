import sys

input = sys.stdin.readline
a,b,c,d=map(int,input().split())
p=list(map(int,input().split()))
for person in p:
    biten=0
    person-=1
    if person%(a+b)<a:
        biten+=1
    if person%(c+d)<c:
        biten+=1
    print(biten)