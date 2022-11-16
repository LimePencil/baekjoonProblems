import sys

input = lambda: sys.stdin.readline().rstrip()
x,y = list(map(int,input().split()))
print(((100-y)/y)/((100-x)/x))