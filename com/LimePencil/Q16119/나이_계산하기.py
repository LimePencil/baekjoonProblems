import sys

input = sys.stdin.readline
arr1 = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))
f =0
if arr1[1]<arr2[1]:
    f=arr2[0]-arr1[0]
elif arr1[1] == arr2[1]:
    if arr1[2]<=arr2[2]:
        f=arr2[0]-arr1[0]
    else:
        f=arr2[0]-arr1[0]-1
else:
    f=arr2[0]-arr1[0]-1
print(f)
print(arr2[0]-arr1[0]+1)
print(arr2[0]-arr1[0])