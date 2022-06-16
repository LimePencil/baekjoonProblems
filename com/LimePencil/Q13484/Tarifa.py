import sys

input = sys.stdin.readline
x=int(input())
n=int(input())
print(x*(n+1)-sum([int(input()) for _ in range(n)]))