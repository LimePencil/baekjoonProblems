ls = list(map(int,input().split(" ")))
sum = 0
for i in ls:
    sum += i**2
print(str(sum%10))