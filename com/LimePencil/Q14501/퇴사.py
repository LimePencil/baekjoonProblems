n=int(input())
table=[]
dp=[]
for _ in range(n):
    a,b=list(map(int,input().split()))
    table.append((a,b))
    dp.append(b)
dp.append(0)
for i in range(n-1,-1,-1):
    if i+table[i][0]>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],table[i][1]+dp[i+table[i][0]])
print(dp[0])