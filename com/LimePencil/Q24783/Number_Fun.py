import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    if a+b==c or abs(a-b)==c or a*b==c or (a%b==0 and a//b==c) or (b%a==0 and b//a==c):
        print("Possible")
    else:
        print("Impossible")