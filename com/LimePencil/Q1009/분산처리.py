import sys

input = sys.stdin.readline
t= int(input())
for _ in range(t):
    n,m = list(map(int,input().split(" ")))
    ans = pow(n,m,10)
    print(10 if ans==0 else ans)