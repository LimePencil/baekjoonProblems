import sys

def find_factor(n):
    factors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            factors.append(i)
    for i in range(len(factors)-1,-1,-1):
        if factors[i]**2!=n:
            factors.append(n//factors[i])
    return factors

input = sys.stdin.readline
p,q = list(map(int,input().split()))
p=find_factor(p)
q=find_factor(q)
for i in p:
    for j in q:
        print(i,j)