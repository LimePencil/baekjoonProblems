import sys

input = sys.stdin.readline
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    print("Yes" if x<24 and y<60 else "No","Yes" if 1<=x<=12 and ((((x==4 or x==6 or x==9 or x==11) and 1<=y<=30) or ((x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12) and 1<=y<=31) or (x==2 and 1<=y<=29)))else "No")