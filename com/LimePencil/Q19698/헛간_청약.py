import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))
print(min(arr[0],(arr[1]//arr[3])*(arr[2]//arr[3])))