import sys

input = sys.stdin.readline
n,k = list(map(int,input().split()))
d,s = list(map(int,input().split()))
diff=(d*n-k*s)/(n-k)
if diff<0 or diff>100:
    print("impossible")
else:
    print(diff)