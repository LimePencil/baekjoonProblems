import sys

input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    m=int(input())
    arr=[list(map(int,input().split())) for _ in range(m)]
    K,D,A=list(map(int, input().split()))
    ans=0
    for i in range(m):
        k,d,a=arr[i]
        ans+=max(0,k*K-d*D+a*A)
    print(ans)