import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))
print(max(arr[2]-arr[1],arr[1]-arr[0])-1)