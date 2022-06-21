import sys

input = sys.stdin.readline
n = int(input())
print("@"*(n+2))
for i in range(n):
    print("@"+" "*n+"@")
print("@"*(n+2))