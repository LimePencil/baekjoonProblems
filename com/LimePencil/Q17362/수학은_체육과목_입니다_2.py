import sys

input = sys.stdin.readline
n = int(input())
n%=8
if n==0:
    print("2")
elif n<=5:
    print(n)
else:
    print(n-(n-5)*2)