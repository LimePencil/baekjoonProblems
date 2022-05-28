import sys

input = sys.stdin.readline
for t in range(int(input())):
    a,b,c=sorted(list(map(int,input().split())))
    if c>=a+b:
        print("Case #{}: invalid!".format(t+1))
    elif a==b and b==c:
        print("Case #{}: equilateral".format(t+1))
    elif (a==b and b!=c)or(b==c and a!=b)or(a==c and b!=a):
        print("Case #{}: isosceles".format(t+1))
    else:
        print("Case #{}: scalene".format(t+1))