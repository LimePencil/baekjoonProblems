import sys

input = lambda: sys.stdin.readline().rstrip()

l=[]
for i in range(1,200):
    for j in range(i+1,200):
        l.append((i**2+j**2,i,j))
l.sort(key=lambda x:(x[0],x[1]))
    
while True:
    a,b = list(map(int,input().split()))
    if a==b==0:
        break
    x=l.index((a**2+b**2,a,b))
    print(l[x+1][1],l[x+1][2])