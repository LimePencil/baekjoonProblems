import sys

input = sys.stdin.readline
a,b,c,d,e = input().split()
a=int(a)
c=int(c)
e=int(e)
ans=[]
p=0
if b=="+":
    p=a+c
elif b=="-":
    p=a-c
elif b=="/":
    p=a//c
else:
    p=a*c
if d=="+":
    p+=e
elif d=="-":
    p-=e
elif d=="/":
    if (p<0 and e>0) or (p>0 and e<0):
        p=abs(p)//abs(e)
        p*=-1
    else:
        p//=e
else:
    p*=e
ans.append(p)
if d=="+":
    p=c+e
elif d=="-":
    p=c-e
elif d=="/":
    p=c//e
else:
    p=c*e
if b=="+":
    p+=a
elif b=="-":
    p=a-p
elif b=="/":
    if (p<0 and a>0) or (p>0 and a<0):
        p=abs(a)//abs(p)
        p*=-1
    else:
        p=a//p
else:
    p*=a
ans.append(p)
print(*sorted(ans),sep="\n")