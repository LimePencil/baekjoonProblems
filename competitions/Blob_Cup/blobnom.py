import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split(" ")))
m = max(arr[0],arr[n-1])
for i in range(1,n-1):
    m = max(m,arr[i]+min(arr[i-1],arr[i+1]))
print(m)