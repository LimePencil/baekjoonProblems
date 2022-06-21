import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    print("@"*n+" "*3*n+"@"*n)
for i in range(n):
    print("@"*n+" "*2*n+"@"*n)
for i in range(n):
    print("@"*n*3)
for i in range(n):
    print("@"*n+" "*2*n+"@"*n)
for i in range(n):
    print("@"*n+" "*3*n+"@"*n)