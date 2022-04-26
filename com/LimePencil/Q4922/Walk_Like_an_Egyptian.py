import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n==0:
        break
    print("{} => {}".format(n,n**2-n+1))