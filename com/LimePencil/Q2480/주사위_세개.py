import sys

arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr.sort()
if arr[0] == arr[1]:
    if arr[1]== arr[2]:
        print(arr[2]*1000+10000)
    else:
        print(arr[1]*100+1000)
elif arr[1]==arr[2]:
    print(arr[1]*100+1000)
else:
    print(arr[2]*100)
