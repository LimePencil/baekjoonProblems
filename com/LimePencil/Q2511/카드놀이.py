arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
a=0
b=0
last="D"
for i in range(10):
    if arr1[i]>arr2[i]:
        a+=3
        last="A"
    elif arr1[i]<arr2[i]:
        b+=3
        last="B"
    else:
        a+=1
        b+=1
print(a,b)
print("A" if a>b else "B" if a<b else last)