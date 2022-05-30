import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(min(arr),max(arr))