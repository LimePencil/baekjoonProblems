import sys

input = sys.stdin.readline
n = int(input())
print(sum([sum(map(int,input().split())) for _ in range(n)]))