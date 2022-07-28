import sys

input = sys.stdin.readline
n = int(input())
s=sum(list(map(int,input().split())))
if s%3==0:
    print("yes")
else:
    print("no")