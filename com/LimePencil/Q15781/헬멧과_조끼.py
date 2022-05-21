import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(max(arr1)+max(arr2))