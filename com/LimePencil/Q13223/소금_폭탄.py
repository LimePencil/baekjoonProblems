from datetime import datetime, timedelta
import sys

input = sys.stdin.readline
h1,m1,s1 = list(map(int,input().split(":")))
h2,m2,s2 = list(map(int,input().split(":")))
t=datetime(2000,1,1,h2,m2,s2)-timedelta(hours=h1,minutes=m1,seconds=s1)
print("24:00:00" if t.strftime("%H:%M:%S") =="00:00:00" else t.strftime("%H:%M:%S"))