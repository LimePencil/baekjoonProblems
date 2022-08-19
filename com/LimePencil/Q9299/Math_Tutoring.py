import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    n,*coef= list(map(int,input().split()))
    ans=[]
    for i in range(n):
        ans.append(coef[i]*(n-i))
    print(f"Case {t}: {n-1}",*ans)
