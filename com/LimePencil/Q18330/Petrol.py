import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
print(min(n,(m+60))*1500+max(0,n-(m+60))*3000)