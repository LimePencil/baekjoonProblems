from math import atan,degrees
import sys

input = sys.stdin.readline
while True:
    a,b,s,m,n=list(map(int,input().split()))
    if a==b==s==n==m==0:
        break
    hor=a*m
    ver=n*b
    print("{:.2f} {:.2f}".format(degrees(atan(ver/hor)),((ver**2+hor**2)**(1/2))/s))