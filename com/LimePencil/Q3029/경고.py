import sys
import datetime

input = sys.stdin.readline
a,b,c = list(map(int,input().split(":")))
d,e,f = list(map(int,input().split(":")))
start=datetime.timedelta(hours=a,minutes=b,seconds=c)
end=datetime.timedelta(hours=d,minutes=e,seconds=f)
duration=end-start
if duration.days==-1:
    duration+=datetime.timedelta(hours=24)
if duration.seconds==0:
    print("24:00:00")
else:
    ans=str(duration)
    if len(ans)<8:
        ans="0"+ans
    print(ans)