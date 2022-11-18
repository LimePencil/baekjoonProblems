import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    s=input()
    n-= "CD" in s
print(n)