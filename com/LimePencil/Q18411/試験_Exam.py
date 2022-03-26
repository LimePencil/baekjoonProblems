import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))
s = sum(arr)
print(s-min(arr))