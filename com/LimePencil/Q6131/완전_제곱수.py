import sys

input = sys.stdin.readline
n = int(input())
cnt=0
for i in range(1,501):
    for j in range(i,501):
        if j**2==n+i**2:
            cnt+=1
print(cnt)