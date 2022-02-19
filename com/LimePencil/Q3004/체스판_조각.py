import sys

n = int(sys.stdin.readline().rstrip("\n"))
w = n//2
h = n-w
print((w+1)*(h+1))