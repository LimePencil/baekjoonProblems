import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    num=input()
    print(len(num))