import sys

input = sys.stdin.readline
for i in range(1,int(input())+1):
    a,b=list(map(int,input().split()))
    print("Case #{}:".format(i),int(b**(1/3))-int((a-1)**(1/3)))