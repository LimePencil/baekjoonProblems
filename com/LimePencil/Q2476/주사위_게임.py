m = 0
for _ in range(int(input())):
    a,b,c= sorted(list(map(int,input().split())))
    if a==b and b ==c:
        m = max(10000+a*1000,m)
    elif a==b or b==c:
        m = max(1000+b*100,m)
    else:
        m = max(c*100,m)
print(m)