import sys

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
print(max(0,arr[0]*arr[1]-arr[2]))