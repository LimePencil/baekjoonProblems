import sys

input = sys.stdin.readline
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    s=sum(arr)
    print(*arr,"Seems OK" if s==180 else "Check")