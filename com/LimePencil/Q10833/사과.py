import sys

input = sys.stdin.readline
ans=0
for _ in range(int(input())):
    a,b= list(map(int,input().split()))
    ans+=b%a
print(ans)