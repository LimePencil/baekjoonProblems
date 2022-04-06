m=-1
x=0
y=0
for i in range(9):
    s=list(map(int,input().split()))
    for j in range(9):
        if s[j]>m:
            x=i+1
            y=j+1
            m=s[j]
print(m)
print(x,y)