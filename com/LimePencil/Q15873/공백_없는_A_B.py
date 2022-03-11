import sys

input = sys.stdin.readline
n = input().rstrip("\n")
num = int(n)
if len(n) ==2:
    print(num//10+num%10)
elif len(n) ==3:
    if n[1] == "0":
        print(num//10+num%10)
    else:
        print(num//100+num%100)
else:
    print("20")