import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))
a,_,_ =list(map(int,input().split()))
print(arr.index(a)+1 if a in arr else 0)