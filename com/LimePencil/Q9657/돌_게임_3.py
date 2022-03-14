import sys

input = sys.stdin.readline
n = int(input())
print("CY" if n%7 ==0 or n%7==2 else "SK")