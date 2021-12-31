import sys

def pow(a,b):
    if b ==1:
        return a%c
    else:
        t = pow(a,b//2)
        if b%2 ==0:
            return t* t%c
        else:
            return t*t*a%c

a,b,c = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(pow(a,b))



