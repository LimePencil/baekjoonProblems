import sys

input = sys.stdin.readline
n = int(input())
ans=[]
s=bin(n)[2:][::-1]
for i,k in enumerate(s):
    if k=="1":
        ans.append(i)
print(*ans)