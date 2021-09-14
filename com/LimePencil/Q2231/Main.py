i = input()
length = len(i)
num = int(i)
ans = 0
for x in range(max(0,num-9*length),num):
    string = str(x)
    sum = 0
    for a in string:
        sum += int(a)
    if(x+sum == num):
        ans = x
        break
print(str(ans))

