import sys

input = sys.stdin.readline
n,a,b = list(map(int,input().split()))
a-=1
b-=1
s=input().rstrip()
ans=""
for i in range(a):
    if 0<=i<n:
        ans+=s[i]
for i in range(b,a-1,-1):
    if 0<=i<n:
        ans+=s[i]
for i in range(b+1,n):
    if 0<=i<n:
        ans+=s[i]
print(ans)