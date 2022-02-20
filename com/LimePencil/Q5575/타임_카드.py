import sys

for _ in range(3):
    arr = list(map(int,input().split(" ")))
    s = (arr[3]-arr[0])*3600+(arr[4]-arr[1])*60+(arr[5]-arr[2])
    m = s//60
    s%=60
    h = m//60
    m%=60
    print(str(h)+" "+str(m)+" "+str(s))