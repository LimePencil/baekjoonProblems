import sys

input = sys.stdin.readline
n = int(input())
o = int(input())
print((o-1)//(n-1)+o,o//(n-1)+o)