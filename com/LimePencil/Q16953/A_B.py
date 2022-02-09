import sys

n,m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
count = 0
while True:
    if m == n:
        count +=1
        break
    elif m > n:
        if m%2 == 0:
            m//=2
            count+=1
        elif m%10 == 1:
            m//=10
            count+=1
        else:
            count= -1
            break
    else:
        count= -1
        break
print(count)
