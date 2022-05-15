import sys

input=sys.stdin.readline
n,m,k = list(map(int,input().split()))a
m-=1
print((k%n-(3-m)%n)%n+1)