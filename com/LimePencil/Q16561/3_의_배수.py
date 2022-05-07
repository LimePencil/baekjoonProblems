import sys

input = sys.stdin.readline
n = int(input())
ans=0
for i in range(3,n+1,3):
    for j in range(3,n-i-2,3):
        ans+=1
print(ans)