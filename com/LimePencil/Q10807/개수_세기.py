import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
v = int(input())
print(arr.count(v))