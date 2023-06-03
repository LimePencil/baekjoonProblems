import sys

input= lambda: sys.stdin.readline().rstrip()
t = int(input())
q=[]
for _ in range(t):
    q.append(list(map(int,input().split())))
    
for i in range(t):
    k,n,m=q[i]
    if k==1:
        if n%2==1 and m%2==1:
            print("cubelover")
        else:
            print("koosaga")
    else:
        if n>m:
            n,m=m,n
        
        if (n-1)%(k+1)==k:
            print("koosaga")
        else:
            if ((n-1)//(k+1))%2==0:
                print("koosaga" if (m-n)%2 else "cubelover")
            else:
                print("koosaga" if (m-n)%2==0 else "cubelover")