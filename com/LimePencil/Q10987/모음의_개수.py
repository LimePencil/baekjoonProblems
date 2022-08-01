import sys

input = sys.stdin.readline
s=input().rstrip()
print(sum(map(s.count, ['a','e','i','o','u'])))