import sys

input = sys.stdin.readline
cnt=0
while True:
    n=int(input())
    cnt+=1
    if n==0:
        break
    print("{}. {} {}".format(cnt,"odd" if n*3%2!=0 else "even",(n-1)//2 if n*3%2!=0 else n//2))  