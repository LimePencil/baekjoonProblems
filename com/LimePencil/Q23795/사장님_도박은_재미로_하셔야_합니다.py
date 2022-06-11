import sys

input = sys.stdin.readline
ans=0
while True:
    n = int(input())
    if n==-1:
        break
    ans+=n
print(ans)