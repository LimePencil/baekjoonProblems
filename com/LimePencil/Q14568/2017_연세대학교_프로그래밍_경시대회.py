import sys

input = sys.stdin.readline
n = int(input())
cnt=0
for i in range(1,n+1):
    for j in range(1,n-i+1):
        if n-i-j==0:
            continue
        if i>j+1 and (n-i-j)%2==0:
            cnt+=1
print(cnt)