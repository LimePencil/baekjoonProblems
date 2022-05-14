import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
ans=[arr[0]]
for i in range(1,n):
    ans.append((i+1)*arr[i]-(i)*arr[i-1])
print(*ans)