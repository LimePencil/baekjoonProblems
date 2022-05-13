import sys

input = sys.stdin.readline

a=0
b=0
c=0
d=0
e=0
for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    if x==0 or y==0:
        e+=1
    elif x>0 and y>0:
        a+=1
    elif x>0 and y<=0:
        d+=1
    elif x<0 and y<=0:
        c+=1
    else:
        b+=1
print("Q1: {}".format(a))
print("Q2: {}".format(b))
print("Q3: {}".format(c))
print("Q4: {}".format(d))
print("AXIS: {}".format(e))