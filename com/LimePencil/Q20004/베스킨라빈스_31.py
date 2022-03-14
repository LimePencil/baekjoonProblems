import sys

input = sys.stdin.readline
n = int(input())
for i in range(1,n+1):
    if 30%(i+1) ==0:
        print(i)