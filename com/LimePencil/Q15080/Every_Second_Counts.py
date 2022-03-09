import sys

input = sys.stdin.readline
arr1 = input().split(" ")
arr2 = input().split(" ")
h = int(arr2[0]) - int(arr1[0])
m = int(arr2[2]) - int(arr1[2])
s = int(arr2[4]) - int(arr1[4])
if s<0:
    s+=60
    m-=1
if m<0:
    m+=60
    h-=1
if h<0:
    h+=24
print(s+m*60+h*3600)