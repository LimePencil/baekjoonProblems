import sys

input = sys.stdin.readline
n,c = list(map(int,input().split()))
t=0
bed=0
cost=0
for _ in range(n):
    a,b=input().split()
    a=int(a)
    t+=a
    if b=="bedroom":
        bed+=a

    if b=="balcony":
        cost+=a/2
    else:
        cost+=a

cost*=c
print(t)
print(bed)
print(cost)