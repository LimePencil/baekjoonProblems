count = 1
pi=3.1415927
while True:
    d,r,t=map(float,input().split())
    if r == 0:
        break  
    dist=d*r*pi/63360
    print("Trip #{}: {:.2f} {:.2f}".format(count,dist,dist/t*3600))
    count+=1