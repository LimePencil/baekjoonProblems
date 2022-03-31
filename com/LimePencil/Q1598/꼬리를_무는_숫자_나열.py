n,m=map(int,input().split())
n-=1
m-=1
print(abs(n//4-m//4)+abs(n%4-m%4))