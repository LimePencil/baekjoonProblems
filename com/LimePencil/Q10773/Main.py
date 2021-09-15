n = int(input())
list = []
sum = 0
for _ in range(n):
    i = int(input())
    sum +=i
    if i == 0:
        a = list.pop()
        sum -= a
    else:
        list.append(i)
print(str(sum))