x,y,z=map(int,input().split())
a,b,c=map(int,input().split())
if a>=x and b>=y and c>=z:
    print("A")
elif a>=x/2 and b>=y and c>=z:
    print("B")
elif b>=y and c>=z:
    print("C")
elif b>=y/2 and c>=z:
    print("D")
else:
    print("E")