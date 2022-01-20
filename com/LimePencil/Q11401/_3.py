import sys
import math

def pow(a,b):
    if b ==1:
        return a%1000000007
    else:
        t = pow(a,b//2)
        if b%2 ==0:
            return t* t%1000000007
        else:
            return t*t*a%1000000007

def fact(a):
    n_f = 1
    for i in range(1,a+1):
        n_f*= i
        n_f %= 1000000007
    return n_f

n, k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
p1 = fact(n) % 1000000007
p2 = pow(fact(k)*fact(n-k),1000000005)% 1000000007
print((p1*p2)% 1000000007)