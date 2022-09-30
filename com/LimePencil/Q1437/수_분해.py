import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
m=10007
if n<5:
    print(n)
elif n%3==0:
    print(pow(3,n//3,m))
elif n%3==1:
    print((pow(3,(n-4)//3,m)*4)%m)
else:
    print((pow(3,(n-2)//3,m)*2)%m)