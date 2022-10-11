import sys

input = lambda: sys.stdin.readline().rstrip()
a,b,c = sorted(list(map(int,input().split())))
print(1 if a+b==c else 2 if a*b==c else 3)