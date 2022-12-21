import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
print(sum([int(input()) for _ in range(n)]))