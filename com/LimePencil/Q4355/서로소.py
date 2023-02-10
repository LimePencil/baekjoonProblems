import sys
import math
input = sys.stdin.readline
while True:
    n = int(input())
    if n==0:
        break
    if n==1:
        print(0)
        continue
    ans=n
    for i in range(2,math.ceil(n**0.5)+1):
        if n%i==0:
            while n%i==0:
                n//=i
            ans*=(i-1)/i
    if n>1:
        ans*=(n-1)/n
    print(round(ans))