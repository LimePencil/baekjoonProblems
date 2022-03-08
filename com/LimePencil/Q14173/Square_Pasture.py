import sys

input = sys.stdin.readline
arr1 = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))
print(max(max(arr1[0],arr1[2],arr2[0],arr2[2])-min(arr1[0],arr1[2],arr2[0],arr2[2]),max(arr1[1],arr1[3],arr2[1],arr2[3])-min(arr1[1],arr1[3],arr2[1],arr2[3]))**2)