import sys

input = sys.stdin.readline
arr1 = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))

print(max(sum(arr1),sum(arr2))) 