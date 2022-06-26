import sys

input = sys.stdin.readline
n = int(input())
print("CY" if n%4 ==0 or n%4==2 else "SK")