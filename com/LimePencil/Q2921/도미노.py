n=int(input())
sum=0
for i in range(0,n+1):
    for j in range(i,n+1):
        sum+=i+j
print(sum)