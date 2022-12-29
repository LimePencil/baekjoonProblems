import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
m = int(input())
for i in range(n,m+1,60):
    print(f"All positions change in year {i}")