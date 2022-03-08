import sys

input = sys.stdin.readline
n = int(input(),2)
m = int(input(),2)
print(bin(n*m)[2:])