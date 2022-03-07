import sys

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
arr.sort()
print(abs(arr[0]+arr[3]-arr[2]-arr[1]))