import sys

input = sys.stdin.readline
while True:
    n=int(input())
    if n==0:
        break
    s=sum(map(int,input().split()))
    print("Mary won {} times and John won {} times".format(n-s,s))