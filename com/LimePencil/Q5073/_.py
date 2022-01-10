import sys

a, b, c = sorted(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
while a!=0 and b!=0 and c!=0:
    if c>=a+b:
        print("Invalid")
    elif a==b and b==c:
        print("Equilateral")
    elif (a==b and b!=c)or(b==c and a!=b)or(a==c and b!=a):
        print("Isosceles")
    else:
        print("Scalene")
    a, b, c = sorted(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))