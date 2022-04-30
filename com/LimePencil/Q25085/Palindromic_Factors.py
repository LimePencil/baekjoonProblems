import math
import sys

input = sys.stdin.readline
for t in range(int(input())):
    n=int(input())
    ans=0
    factors=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            factors.append(i)
            if i!=n//i:
                factors.append(n//i)
    factors.sort()
    for f in factors:
        if str(f)==str(f)[::-1]:
            ans+=1

    print("Case #{}: {}".format(t+1,ans))