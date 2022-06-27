import sys

input = sys.stdin.readline
h1,m1 = list(map(int,input().split()))
h2,m2 = list(map(int,input().split()))
n=input().rstrip()
ans=0
while not (h1==h2 and m1==m2):
    if n in str(h1) or n in str(m1) or ((h1<10 or m1<10) and n=="0"):
        ans+=1
    m1+=1
    if m1==60:
        m1=0
        h1+=1
if n in str(h1) or n in str(m1):
    ans+=1
print(ans)