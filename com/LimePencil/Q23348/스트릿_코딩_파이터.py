import sys

input = sys.stdin.readline
a,b,c = list(map(int,input().split()))
m=0
for _ in range(int(input())):
    s=0
    for i in range(3):
        d,e,f=list(map(int,input().split()))
        s+=d*a+e*b+f*c
    m=max(s,m)

print(m)
