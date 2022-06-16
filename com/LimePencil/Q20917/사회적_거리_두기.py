import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,c = list(map(int,input().rstrip().split()))
    modem=list(map(int,input().rstrip().split()))
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