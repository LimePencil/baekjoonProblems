import sys

input = lambda: sys.stdin.readline().rstrip()
x,y = list(map(int,input().split()))
print(x+y if x>y else y-x)