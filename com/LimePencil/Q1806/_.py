import sys

n,s = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

start = 0
end = 0
sum = 0
length = float('inf')
while True:
    if sum >= s:
        length = min(length,end-start)
        sum -= arr[start]
        start+=1

    elif end == n:
       break  
    else:
        sum += arr[end]
        end+=1 

        
print(length if length != float('inf') else 0)
