import sys

input = lambda: sys.stdin.readline().rstrip()
s=input()
n = int(input())
arr = [input() for _ in range(n)]
print(arr.count(s))