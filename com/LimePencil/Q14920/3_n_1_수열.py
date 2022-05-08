import sys

input = sys.stdin.readline
n = int(input())
cnt=1
while n!=1:
    cnt+=1
    if n%2==0:
        n//=2
    else:
        n=3*n+1
print(cnt)