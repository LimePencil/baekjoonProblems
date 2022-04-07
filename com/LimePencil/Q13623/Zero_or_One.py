a,b,c=map(int,input().split())
s=a+b+c
print("*" if s==0 or s==3 else "A" if a!=b and a!=c else "B" if b!=c and b!=a else "C")