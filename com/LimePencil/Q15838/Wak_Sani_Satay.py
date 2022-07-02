from math import ceil
import sys

input = sys.stdin.readline
cnt=0
while True:
    n = int(input())
    cnt+=1
    if n==0:
        break
    c=0
    b=0
    l=0
    i=0
    for _ in range(n):
        arr = list(map(int,input().split()))
        c+=arr[0]
        b+=arr[1]
        l+=arr[2]
        i+=arr[3]
    c_k=c/85
    b_k=b/85
    l_k=l/85
    print("Case #{}: RM{:.2f}".format(cnt,i*0.6+c*0.8-15.5*c_k+b*1-32*b_k+l*1.2-40*l_k))