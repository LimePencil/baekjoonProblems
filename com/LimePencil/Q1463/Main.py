def find_min_count(ls,num):
    comparison = []
    if(num%3 ==0):
        comparison.append(ls[int(num/3)])
    if num%2 ==0:
        comparison.append(ls[int(num/2)])
    comparison.append(ls[num -1])
    m=min(comparison)
    ls.append(m+1)

n = int(input())
list=[0,0,1,1]
for i in range(4,n+1):
    find_min_count(list,i)
print(list[n])
