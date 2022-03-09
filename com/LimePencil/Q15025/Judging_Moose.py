import sys

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
if n ==0 and m==0:
    print("Not a moose")
elif n==m:
    print("Even {}".format(n*2))
else:
    print("Odd {}".format(max(n,m)*2))