import sys

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
print(arr[2]//(arr[0]*2)*arr[1])