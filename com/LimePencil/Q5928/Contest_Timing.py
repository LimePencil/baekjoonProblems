import sys

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
m = (arr[0]-11)*24*60+(arr[1]-11)*60+(arr[2]-11)
if m >=0:
    print(m)
else:
    print(-1)