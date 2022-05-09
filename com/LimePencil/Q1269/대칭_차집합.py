import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
print(len(a.difference(b)) + len(b.difference(a)))