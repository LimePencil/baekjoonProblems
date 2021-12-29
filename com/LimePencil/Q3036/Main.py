import sys

n = int(sys.stdin.readline().rstrip("\n"))

rings = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
for i in range(1,n):
    l =[rings[0],rings[i]]
    l.sort()
    a,b = l
    while a !=0:
        temp = a
        a=b%a
        b=temp
    print(str(rings[0]//b)+"/"+str(rings[i]//b))