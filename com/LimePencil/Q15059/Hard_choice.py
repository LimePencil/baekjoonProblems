import sys

input = sys.stdin.readline
arr1 = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))
print(sum([max(0,arr2[i] - arr1[i]) for i in range(3)]))