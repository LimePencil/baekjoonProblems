import sys

input = sys.stdin.readline
n,m= list(map(int,input().split()))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    a=list(map(int,input().split()))
    for j in range(m):
        arr[i][j]+=a[j]
for i in range(n):
    print(*arr[i])