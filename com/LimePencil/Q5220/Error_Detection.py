import sys

input = sys.stdin.readline

for _ in range(int(input())):
    num,check=map(int,input().split())
    num=sum(map(int,list("{0:016b}".format(num))))
    if num%2==check:
        print("Valid")
    else:
        print("Corrupt")