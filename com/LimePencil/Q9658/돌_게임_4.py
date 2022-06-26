import sys

input = sys.stdin.readline
n = int(input())
print("CY" if n%7 ==1 or n%7==3 else "SK")