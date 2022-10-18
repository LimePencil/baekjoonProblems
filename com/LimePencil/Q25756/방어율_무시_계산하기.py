import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
musi=0
for i in range(n):
    musi=(1-(1-musi/100)*(1-arr[i]/100))*100
    print(musi)