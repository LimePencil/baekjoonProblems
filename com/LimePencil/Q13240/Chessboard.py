import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
for i in range(n):
    if i%2==0:
        print("*."*(m//2)+"*"*(m%2))
    else:
        print(".*"*(m//2)+"."*(m%2))