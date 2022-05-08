import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
ans="Accepted"
for i in range(n):
    a,b=list(map(int,input().split()))
    if a!=b:
        ans="Wrong Answer"
        break
if ans=="Accepted":
    for i in range(m):
        a,b=list(map(int,input().split()))
        if a!=b:
            ans="Why Wrong!!!"
            break
print(ans)