a=[sum(map(int,input().split()))for _ in range(5)]
m=max(a)
print(a.index(m)+1,m)