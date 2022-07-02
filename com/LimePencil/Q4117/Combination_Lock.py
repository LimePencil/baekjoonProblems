import sys

input = sys.stdin.readline

while True:
    n,t1,t2,t3=list(map(int,input().split()))
    if n==0:
        break
    print(n*4-1+(t2-t1)%n+(t2-t3)%n)