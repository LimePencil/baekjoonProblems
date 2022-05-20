import sys

input = sys.stdin.readline
for _ in range(int(input())):
    ans = 0
    n,k= list(map(int,input().split()))
    arr = list(map(int,input().split()))
    for i in arr:
        ans+=i//k
    print(ans)