sum=0
n1=0
for _ in range(10):
    num=int(input())
    sum+=num
    if sum>=100:
        n2=sum
        break
    else:
        n1=sum
        n2=0
if n2>0:
    if(n2-100)<=(100-n1):
        print(n2)
    else:
        print(n1)
elif n2==0:
    print(n1)