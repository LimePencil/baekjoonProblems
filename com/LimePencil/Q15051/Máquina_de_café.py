import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
k = int(input())
print(min(m*2+k*4,n*2+k*2,n*4+m*2))