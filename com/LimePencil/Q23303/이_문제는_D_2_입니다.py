import sys

input = sys.stdin.readline
s = input().rstrip()
if "d2" in s or "D2" in s:
    print("D2")
else:
    print("unrated")