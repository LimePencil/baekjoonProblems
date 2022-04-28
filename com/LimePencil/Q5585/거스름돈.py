import sys

input = sys.stdin.readline
n = int(input())
n=1000-n
ans=0
ans+=n//500
n-=n//500*500
ans+=n//100
n-=n//100*100
ans+=n//50
n-=n//50*50
ans+=n//10
n-=n//10*10
ans+=n//5
n-=n//5*5
ans+=n//1
n-=n//1
print(ans)