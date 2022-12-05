import sys
input = lambda: sys.stdin.readline().rstrip()

def gcd(c,d):
    while d:
        c,d=d,c%d
    return c

a,b = list(map(int,input().split()))
m=a*b
for i in range(int(m**0.5),a-1,-1):
    if m%i==0 and gcd(i,m//i)==a:
        print(i,m//i)
        break