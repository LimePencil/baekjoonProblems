import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c,d,e=list(map(int,input().split()))
    print("${:.2f}".format(a*350.34+b*230.90+c*190.55+d*125.30+e*180.90))