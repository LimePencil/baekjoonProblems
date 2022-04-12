import sys
input = sys.stdin.readline
a = list(input().rstrip())
o = input().rstrip()
b = list(input().rstrip())
if o=="*":
    print("1"+"0"*(len(a)+len(b)-2))
else:
    if a==b:
        a[0]=2
        print(*a,sep="")
    else:
        if len(b)>len(a):
            a,b=b,a
        a[len(a)-len(b)]=1
        print(*a,sep="")