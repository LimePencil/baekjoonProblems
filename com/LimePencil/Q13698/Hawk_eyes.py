import sys

input = sys.stdin.readline
s = input().rstrip()
arr=[1,0,0,2]
for i in s:
    if i=="A":
        temp=arr[0]
        arr[0]=arr[1]
        arr[1]=temp
    elif i=="B":
        temp=arr[0]
        arr[0]=arr[2]
        arr[2]=temp
    elif i=="C":
        temp=arr[0]
        arr[0]=arr[3]
        arr[3]=temp
    elif i=="D":
        temp=arr[1]
        arr[1]=arr[2]
        arr[2]=temp
    elif i=="E":
        temp=arr[3]
        arr[3]=arr[1]
        arr[1]=temp
    else:
        temp=arr[3]
        arr[3]=arr[2]
        arr[2]=temp
print(arr.index(1)+1)
print(arr.index(2)+1)