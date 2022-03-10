import sys

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
up = arr[0]*arr[2]
down = arr[1]*arr[3]*2
if float.is_integer(up/down):
    print("1")
else:
    print("0")