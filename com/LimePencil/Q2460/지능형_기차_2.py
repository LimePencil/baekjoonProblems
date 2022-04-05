mx = 0
m = 0
for _ in range(10):
    a,b = list(map(int,input().split()))
    m+=b-a
    mx = max(m,mx)
print(mx)