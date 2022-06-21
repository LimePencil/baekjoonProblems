import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    print("@"*(n*5))
for i in range(n*3):
    print("@"*n)
for i in range(n):
    print("@"*(n*5))