import sys

n,c = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
modem=[]
for _ in range(n):
    modem.append(int(sys.stdin.readline().rstrip("\n")))
modem.sort()
low = 1
high = modem[n-1] - modem[0] +1
while low<high:
    mid = (low+high)//2
    count = 1
    lasthouse = modem[0]
    for i in range(1,n):
        curr = modem[i]
        if curr-lasthouse >=mid:
            count +=1
            lasthouse = curr
    if count < c:
        high = mid
    else:
        low = mid+1
print(low-1)