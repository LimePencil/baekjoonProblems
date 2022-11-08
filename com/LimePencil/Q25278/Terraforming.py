import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
temp=-30
water=0
oxygen=0
for _ in range(n):
    a,b = input().split()
    b=int(b[1])
    if a=="temperature":
        temp+=b
    elif a=="oxygen":
        oxygen+=b
    else:
        water+=b
if temp>=8 and water>=9 and oxygen>=14:
    print("liveable")
else:
    print("not liveable")