import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a,b= list(map(int,input().split()))
    print((a//b)**2)