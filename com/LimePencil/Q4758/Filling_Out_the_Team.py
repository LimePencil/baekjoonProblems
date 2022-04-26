import sys

input = sys.stdin.readline
while True:
    a,b,c = list(map(float,input().split()))
    if a==0 and b==0 and c==0:
        break
    ans=[]
    if a<=4.5 and b>=150 and c>=200:
        ans.append("Wide Receiver")
    if a<=6.0 and b>=300 and c>=500:
        ans.append("Lineman")
    if a<=5.0 and b>=200 and c>=300:
        ans.append("Quarterback")
    if len(ans)==0:
       print("No positions") 
    else:
        print(" ".join(ans))