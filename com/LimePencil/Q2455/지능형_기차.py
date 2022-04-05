mx = 0
m = 0
for _ in range(4):
    a,b = list(map(int,input().split()))
    m+=b-a
    mx = max(m,mx)
print(mx)