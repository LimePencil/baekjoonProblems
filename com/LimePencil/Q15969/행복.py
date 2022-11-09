import sys

input = lambda: sys.stdin.readline().rstrip()
n=int(input())
arr = list(map(int,input().split()))
print(max(arr)-min(arr))