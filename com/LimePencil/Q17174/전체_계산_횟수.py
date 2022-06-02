import sys

input = sys.stdin.readline
a,b = list(map(int,input().split()))
ans=a
while a!=0:
    ans+=a//b
    a//=b
print(ans)