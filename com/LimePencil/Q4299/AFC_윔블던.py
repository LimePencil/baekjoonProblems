import sys

n,m = map(int,sys.stdin.readline().rstrip("\n").split(" "))
if m>n or(n+m)%2 or (n-m)%2 ==1:
    print(-1)
else:
    print(str((n+m)//2)+" "+str((n-m)//2))