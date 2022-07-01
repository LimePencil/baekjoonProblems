import sys

input = sys.stdin.readline
w,h,x,y,p = list(map(int,input().split()))
cnt=0
for _ in range(p):
    a,b=list(map(int,input().split()))
    if (x<=a<=x+w and y<=b<=y+h) or ((x-a)**2+(y+h/2-b)**2<=(h/2)**2) or ((x+w-a)**2+(y+h/2-b)**2<=(h/2)**2):
        cnt+=1
    
print(cnt)