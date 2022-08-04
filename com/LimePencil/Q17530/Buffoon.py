import sys

input = sys.stdin.readline
l=[int(input()) for _ in range(int(input()))]
print("S" if max(l)==l[0] else "N")