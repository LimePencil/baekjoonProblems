import sys

a,b = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
c= int(sys.stdin.readline().rstrip("\n"))
hour_added = (b+c)//60
minute_added = (b+c)%60
new_hour = (a+hour_added)%24
new_mimute = minute_added
print(str(new_hour) + " "+ str(new_mimute))
