n = int(input())
arr = list(map(int,input().split()))
y=0
m=0
for a in arr:
    y+=a//30*10+10
    m+=a//60*15+15
if y>m:
    print("M {}".format(m))
elif y<m:
    print("Y {}".format(y))
else:
    print("Y M {}".format(m))