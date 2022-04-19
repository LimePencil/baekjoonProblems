import sys

input = sys.stdin.readline
a,b,c= list(map(int,input().split()))
if a+b==c:
    print(a,"+",b,"=",c,sep="")
elif a-b==c:
    print(a,"-",b,"=",c,sep="")
elif a*b==c:
    print(a,"*",b,"=",c,sep="")
elif a%b==0 and a//b==c:
    print(a,"/",b,"=",c,sep="")
elif a==b+c:
    print(a,"=",b,"+",c,sep="")
elif a==b-c:
    print(a,"=",b,"-",c,sep="")
elif a==b*c:
    print(a,"=",b,"*",c,sep="")
elif b%c==0 and a==b//c:
    print(a,"=",b,"/",c,sep="")