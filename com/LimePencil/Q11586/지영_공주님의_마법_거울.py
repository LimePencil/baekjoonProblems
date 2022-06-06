import sys

input = sys.stdin.readline
n = int(input())
s=[]
for _ in range(n):
    s.append(input().rstrip())
m=int(input())
if m==1:
    for i in range(n):
        print(s[i])
elif m==2:
    for i in range(n):
        print(s[i][::-1])
else:
    for i in range(n-1,-1,-1):
        print(s[i])