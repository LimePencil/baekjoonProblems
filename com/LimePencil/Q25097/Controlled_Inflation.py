import sys

input = sys.stdin.readline
for t in range(int(input())):
    n,m=list(map(int,input().split()))
    costom=[]
    for i in range(n):
        a=sorted(list(map(int,input().split())))
        costom.append((a[0],a[-1],a[-1]-a[0]))
    m=float('inf')
    amount_first=costom[0][1]
    amount_second=costom[0][1]
    for i in range(1,n):
        if i==1:
            a=abs(costom[i][1]-costom[i-1][1])+costom[i][2]+amount_second
            b=float('inf')
            c=abs(costom[i][0]-costom[i-1][1])+costom[i][2]+amount_second
            d=float('inf')
        else:
            a=abs(costom[i][1]-costom[i-1][1])+costom[i][2]+amount_second
            b=abs(costom[i][1]-costom[i-1][0])+costom[i][2]+amount_first
            c=abs(costom[i][0]-costom[i-1][1])+costom[i][2]+amount_second
            d=abs(costom[i][0]-costom[i-1][0])+costom[i][2]+amount_first
        amount_first=min(a,b)
        amount_second=min(c,d)
    
    print("Case #{}: {}".format(t+1,min(amount_first,amount_second)))