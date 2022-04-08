a,b=map(int,input().split())
c,d=map(int,input().split())
print(sorted([[a/c+b/d,0],[c/d+a/b,1],[d/b+c/a,2],[b/a+d/c,3]])[-1][1])