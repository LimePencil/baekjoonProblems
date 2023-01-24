import sys

input = lambda: sys.stdin.readline().rstrip()
s=input()
print(s.strip("0").count("0"))