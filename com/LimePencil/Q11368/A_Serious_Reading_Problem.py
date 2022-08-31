import sys

input = sys.stdin.readline
while True:
    c,w,l,p = list(map(int,input().split()))
    if c==w==l==p==0:
        break
    print(c**(w*l*p))