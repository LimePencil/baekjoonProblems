import sys

input = sys.stdin.readline
n = int(input())
print(n-sum([int(input()) for _ in range(9)]))