import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    print(sum(list(map(int,input().split()))))