import sys

input = sys.stdin.readline
k,w,m = map(int,input().split(" "))
print(-((k-w)//m))