import sys

input = sys.stdin.readline
arr = input().split(" ")
print("YES" if int(arr[0])+int(arr[2]) == int(arr[4]) else "NO")