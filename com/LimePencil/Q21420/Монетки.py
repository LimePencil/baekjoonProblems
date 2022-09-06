import sys

input = sys.stdin.readline
coins=[int(input()) for _ in range(int(input()))]
print(min(coins.count(0),coins.count(1)))