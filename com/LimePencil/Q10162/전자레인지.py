import sys

input = sys.stdin.readline
n = int(input())
if n%10 !=0:
    print(-1)
else:
    a= n//300
    b = (n-a*300)//60
    c = (n-(a*300+b*60))//10
    print("{} {} {}".format(a,b,c))