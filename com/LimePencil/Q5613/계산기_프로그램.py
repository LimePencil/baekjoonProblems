import sys

input = sys.stdin.readline
ans=int(input())
while True:
    sign=input().strip()
    if sign=="=":
        break
    num=int(input())
    if sign=="+":
        ans+=num
    elif sign=="-":
        ans-=num
    elif sign=="*":
        ans*=num
    else:
        ans//=num
print(ans)