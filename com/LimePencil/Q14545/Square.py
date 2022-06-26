import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    print(n*(n+1)*(2*n+1)//6)