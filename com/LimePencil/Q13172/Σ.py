import sys


def pow(a,b):
    if b ==1:
        return a%X
    else:
        t = pow(a,b//2)
        if b%2 ==0:
            return t* t%X
        else:
            return t*t*a%X
n = int(sys.stdin.readline().rstrip("\n"))
arr = []
sum = 0
X = 1000000007
for _ in range(n):
    den,num = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    sum +=(num*pow(den,X-2))%X
    sum%=X
print(sum)