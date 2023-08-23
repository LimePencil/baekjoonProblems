import sys

input = lambda: sys.stdin.readline().rstrip()
h,i,a,r,c = list(map(int,input().split()))
print(h*i-a*r*c)
