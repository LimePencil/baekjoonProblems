import sys

input = sys.stdin.readline
b = input().rstrip("\n")
print(bin(int(b,2)*17,)[2:])