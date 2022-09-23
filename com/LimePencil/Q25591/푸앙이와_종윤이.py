import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
print(100-n,100-m,n+m-100,(100-n)*(100-m),(100-n)*(100-m)//100,(100-n)*(100-m)%100)
print(n+m-100+(100-n)*(100-m)//100,(100-n)*(100-m)%100)