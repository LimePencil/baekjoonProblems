import sys

input = sys.stdin.readline
for _ in range(int(input())):
    print(sum([max(max(list(map(int,input().split()))),0) for _ in range(int(input()))]))