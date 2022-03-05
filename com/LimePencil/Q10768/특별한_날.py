import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
if n== 2 and m ==18:
    print("Special")
elif n<2 or (n==2 and m<18):
    print("Before")
else:
    print("After")