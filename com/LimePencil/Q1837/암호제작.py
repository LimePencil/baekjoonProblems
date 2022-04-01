p,k = map(int,input().split())
good = True
for i in range(2,k):
    if p%i==0:
        good = False
        break
print("GOOD" if good else "BAD {}".format(i))