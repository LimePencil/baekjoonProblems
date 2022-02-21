import sys
input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
e= 0
s = 0
m = 0
for _ in range(n):
    for c in input().rstrip("\n"):
        if c == "E":
            e+=1
        elif c=="S":
            s+=1
        else:
            m+=1
print((e*s*m)%(1000000007))
