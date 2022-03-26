import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))
print(1 if sum(arr)<5 else 2)