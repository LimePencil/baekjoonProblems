import sys

input = lambda: sys.stdin.readline().rstrip()
c,n = list(map(int,input().split()))
items = []
min_price = [float('inf')]*(1000+100+1)
min_price[0]=0
for i in range(n):
    items.append(list(map(int,input().split())))
for price, customer in items:
    for i in range(customer,len(min_price)):
        min_price[i]=min(min_price[i],min_price[i-customer]+price)
print(min(min_price[c:c+101]))