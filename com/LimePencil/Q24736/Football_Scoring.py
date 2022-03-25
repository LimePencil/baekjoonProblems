import sys

input = sys.stdin.readline
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(arr1[0]*6+arr1[1]*3+arr1[2]*2+arr1[3]*1+arr1[4]*2,arr2[0]*6+arr2[1]*3+arr2[2]*2+arr2[3]*1+arr2[4]*2)