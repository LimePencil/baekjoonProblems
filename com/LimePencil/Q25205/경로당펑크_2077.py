import sys

input = sys.stdin.readline
n = int(input())
s=input().rstrip()
if s[-1] in "rsefaqtdwczxvg":
    print(1)
else:
    print(0)