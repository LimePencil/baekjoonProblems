n,m=map(int,input().split())
arr1=[]
arr2=[]

for i in range(n):
    if i!=n-1:
        arr1.append(int(input()))
    else:
        arr2=list(map(int,input().split()))
        arr1.append(arr2[0])
        
print(arr1.index(min(arr1))+1,arr2.index(min(arr2))+1)
