import sys

n = int(sys.stdin.readline().rstrip("\n"))
distance = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
price = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

money = 0
curr_price = price[0]

for i in range(len(price)-1):
    if curr_price > price[i]:
        curr_price = price[i]
    else:
        price[i]= curr_price
    money += price[i]*distance[i]

print(money)
