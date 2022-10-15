import sys

input = lambda: sys.stdin.readline().rstrip()
for i in range(1,int(input())+1):
    n=int(input())
    s=input()
    ans=[1]*n
    for j in range(1,n):
        if ord(s[j])>ord(s[j-1]):
            ans[j]=ans[j-1]+1
        else:
            ans[j]=1
    print(f"Case #{i}:",*ans)