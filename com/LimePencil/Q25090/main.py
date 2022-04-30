import sys

input = sys.stdin.readline
n = int(input())
for t in range(1,n+1):
    dice = int(input())
    ans = 0
    streak = 1
    arr = list(map(int,input().split()))
    arr.sort()
    for v in arr:
        if streak<=v:
            ans+=1
            streak+=1
    print("Case #{}: {}".format(t,ans))