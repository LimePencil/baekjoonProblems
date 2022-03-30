n=1
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==n:
        n=b
    elif b==n:
        n=a
print(n)