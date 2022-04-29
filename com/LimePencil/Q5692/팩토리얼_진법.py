from math import factorial
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n==0:
        break
    cnt=1
    ans=0
    while n>0:
        a=n%10
        n//=10
        ans+=factorial(cnt)*a
        cnt+=1
    print(ans)