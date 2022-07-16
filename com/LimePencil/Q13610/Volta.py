import sys

input = sys.stdin.readline
x,y = list(map(int,input().split()))
ans=1+(x//(y-x) if x%(y-x)==0 else x//(y-x)+1)
print(ans)