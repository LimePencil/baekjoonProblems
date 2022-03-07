import sys

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
arr.sort()
if arr[0] == arr[1] or arr[1] == arr[2] or arr[0]+arr[1] == arr[2]:
    print("S")
else:
    print("N")