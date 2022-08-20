import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))
ans=0
for i in range(10):
    for j in range(i+1,10):
        ans^=arr[i]|arr[j]
        for k in range(j+1,10):
            ans^=arr[i]|arr[j]|arr[k]
print(ans)