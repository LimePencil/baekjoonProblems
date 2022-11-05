import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    print(*arr)
    print("both" if 17 in arr and 18 in arr else "zack" if 17 in arr else "mack" if 18 in arr else "none")