def find_min_count(ls,s,num):
    comparison = []
    if(num%3 ==0):
        comparison.append((ls[num//3],num//3))
    if num%2 ==0:
        comparison.append((ls[num//2],num//2))
    comparison.append((ls[num -1],num-1))
    comparison.sort()
    ls.append(comparison[0][0]+1)
    s.append(comparison[0][1])

n = int(input())
list=[0,0,1,1]
steps = [0,0,1,1]
for i in range(4,n+1):
    find_min_count(list,steps,i)
print(list[n])
a = [n]
if n ==1:
    a = []

b = steps[n]
while b>1:
    a.append(b)
    b=steps[b]
a.append(1)
print(*a)

