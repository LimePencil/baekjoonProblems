a,m,k=map(int, input().split())

print(("X" if (k-a)//m+1 <=0 else(k-a)//m+1) if (k-a)%m==0 else "X")