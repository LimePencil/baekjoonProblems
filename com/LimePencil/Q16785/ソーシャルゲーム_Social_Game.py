import sys

input = sys.stdin.readline
a,b,c = list(map(int,input().split()))
n=0
i=0
while n<c:
    i+=1
    n+=a
    if i%7==0:
        n+=b
print(i)