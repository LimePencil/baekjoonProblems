import sys
import datetime

input = sys.stdin.readline
while True:
    s,e = input().split()
    s_m,s_s=map(int,s.split(":"))
    e_m,e_s=map(int,e.split(":"))
    if s_m==0 and s_s==0 and e_m==0 and e_s==0:
        break
    s=datetime.timedelta(hours=s_m,minutes=s_s)
    e=datetime.timedelta(hours=e_m,minutes=e_s)
    x=s+e
    h=str(x.seconds//3600)
    m=str(x.seconds//60%60)
    if len(h)==1:
        h="0"+h
    if len(m)==1:
        m="0"+m
    if x.days>=1:
        m+=" +{}".format(x.days)
    print("{}:{}".format(h,m))