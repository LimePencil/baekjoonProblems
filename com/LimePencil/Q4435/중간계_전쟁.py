import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    q,w,e,r,t,y=list(map(int,input().split()))
    a,s,d,f,g,h,j=list(map(int,input().split()))
    good=q+w*2+e*3+r*3+t*4+y*10
    evil=a+s*2+d*2+f*2+g*3+h*5+j*10
    print("Battle {}: {}".format(i+1,"Evil eradicates all trace of Good" if evil>good else ("Good triumphs over Evil" if good>evil else "No victor on this battle field")))