import sys

input = lambda: sys.stdin.readline().rstrip()
arr = list(map(int,input().split()))
print("S" if 9 not in arr else "F")