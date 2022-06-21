import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    print("@"*(n*3)+" "*n+"@"*n)
for i in range(n*3):
    print("@"*n+" "*n+"@"*n+" "*n+"@"*n)
for i in range(n):
    print("@"*n+" "*n+"@"*(3*n))