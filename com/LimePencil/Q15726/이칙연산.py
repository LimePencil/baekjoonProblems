import sys

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
print(max(arr[0]*arr[1]//arr[2],arr[0]*arr[2]//arr[1]))