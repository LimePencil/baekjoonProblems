import sys

input = sys.stdin.readline
h,m = list(map(int,input().split(":")))
t=240
curr=0
while curr!=t:
    if 7<=h<10 or 15<=h<19:
        curr+=10
    else:
        curr+=20 
    m+=10
    h+=m//60
    m%=60
    h%=24
print(f"{h:02d}:{m:02d}")