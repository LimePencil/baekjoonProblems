import sys

n = int(sys.stdin.readline().rstrip("\n"))

arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
largest = [0]*n
largest[0] = arr[0]
maximum = largest[0]
for a in range(1,n):
    largest[a]= max(arr[a],largest[a-1]+arr[a])
    maximum = max(maximum,largest[a])
print(maximum)