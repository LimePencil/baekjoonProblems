import sys

input = lambda: sys.stdin.readline().rstrip()
g,p,t = list(map(int,input().split()))
one=g+t*p
two=g*p
print(1 if one>two else 2 if one<two else 0)