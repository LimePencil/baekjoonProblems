import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n==-1:
        break
    ans=0
    time_passed=0
    for _ in range(n):
        s,t=map(int,input().split())
        ans+=s*(t-time_passed)
        time_passed=t
    print("{} miles".format(ans))