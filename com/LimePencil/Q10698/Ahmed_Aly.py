import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    a,b,c,d,e= input().split()
    a= int(a)
    c=int(c)
    e=int(e)
    ans=0
    if b=="+":
        ans+=a+c
    else:
        ans+=a-c
    equal="YES" if ans==e else "NO"
    print(f"Case {t}: {equal}")