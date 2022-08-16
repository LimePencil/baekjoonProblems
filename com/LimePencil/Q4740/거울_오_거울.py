import sys

input = sys.stdin.readline
while True:
    s=input().rstrip("\n")
    if s=="***":
        break
    print(s[::-1])