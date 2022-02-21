import sys

input = sys.stdin.readline
n,m = list(map(int,input().split(" ")))
n*=1000
m*=1000
if m+m*2+m*4<=n:
    print(m+m*2+m*4)
elif m//2+m+m*2<=n:
    print(m//2+m+m*2)
elif m//4+m//2+m<=n:
    print(m//4+m//2+m)
else:
    print("0")