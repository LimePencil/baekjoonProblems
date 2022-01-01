import sys
import math

def Sieve(n):
    prime = [True for i in range(n + 1)]
    l = []
    p = 2
    while (p <= n):
        if (prime[p] == True):
            l.append(p)
            if p*p <=n:
                for i in range(p**2, n + 1, p):
                    prime[i] = False
        p += 1
    return l

n = int(sys.stdin.readline().rstrip("\n"))
s= math.ceil((n+1)**0.5*2)
l = Sieve(s)
for i in range(len(l)-1):
    if l[i]*l[i+1] > n:
        print(l[i]*l[i+1])
        break