import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    for i in range(0,n):
        if i==0 or i==n-1:
            print("#"*n)
        else:
            print("#"+"J"*(n-2)+"#")
    print()