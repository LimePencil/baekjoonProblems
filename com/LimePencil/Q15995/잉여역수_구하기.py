import sys

input = sys.stdin.readline
a,m = list(map(int,input().split()))
a_inv=1
while True:
    if a*a_inv%m==1:
        print(a_inv)
        break
    a_inv+=1