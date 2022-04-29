import sys
import math

input = sys.stdin.readline
n = int(input())
gcd=0
if n==2:
    a,b = list(map(int,input().split()))
    gcd=math.gcd(a,b)
elif n==3:
    a,b,c = list(map(int,input().split()))
    gcd=math.gcd(a,math.gcd(b,c))
for i in range(1,gcd+1):
    if gcd%i==0:
        print(i)