import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
x = 2*n+2*m*3.141592
print(int(x) if float.is_integer(x) else x)