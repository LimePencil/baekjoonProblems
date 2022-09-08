import sys

input = sys.stdin.readline
ans=0
for _ in range(int(input())):
    ans +=max(0,max(list(map(int,input().split()))))
print(ans)