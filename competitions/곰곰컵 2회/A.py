import sys

input = lambda: sys.stdin.readline().rstrip()

ans=0
for i in range(int(input())):
    d=int(input().split("-")[1])
    if d<91:
        ans+=1
print(ans)
