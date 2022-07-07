import sys

input = sys.stdin.readline
n = int(input())
if n==0:
    print(1)
elif n==1:
    print(0)
else:
    print(("4" if n%2==1 else "")+"8"*(n//2))