import sys

input = sys.stdin.readline
n = int(input())
if n == 1:
    print("*")
else:
    print(" "*(n-1)+"*")
    for i in range(2,n+1):
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")