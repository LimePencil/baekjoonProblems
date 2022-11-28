import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())

for _ in range(n):
    arr = list(map(int,input().split()))
    s=arr[0]
    arr=arr[1:]
    for i in range(1,s-1):
        if arr[i]!=arr[i-1]+1:
            print(i+1)
            break