import sys

def recur(n,k):
    if k==1:
        return n-1
    if n==1:
        return 0
    elif n<k:
        return (recur(n-1,k)+k)%n
    else:
        temp=recur(n-n//k,k)-n%k
        if temp<0:
            return temp+n
        else:
            return k*temp//(k-1)
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
n,k=map(int,input().split())
print(recur(n,k)+1)