a = int(input())
if a==0:
    print(0)
elif a%2==0 and a<0:
    print(-1)
else:
    print(1)
a=abs(a)
if a==0:
    print("0")
elif a == 1:
    print("1")
else:
    prevprev=0
    prev=1
    mod=1000000000
    for i in range(2,a+1):
        temp=(prevprev%mod+prev%mod)%mod
        prevprev=prev
        prev=temp
    print(prev)