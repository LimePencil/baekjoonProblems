import sys

input = sys.stdin.readline

n = int(input())
s=list(map(int,input().split()))
par=5*(n//2)+2*(n%2)
for i in range(n):
    s[i]=min(s[i],7)
print(sum(s)-par)