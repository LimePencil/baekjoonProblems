import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n==0:
        break
    if n>5000000:
        n*=0.8
    elif n>1000000:
        n*=0.9
    print(int(n))