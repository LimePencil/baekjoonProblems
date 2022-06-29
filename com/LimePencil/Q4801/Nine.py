from math import ceil
import sys

input = sys.stdin.readline
while True:
    m,s = list(map(int,input().split(":")))
    if s==0 and m==0:
        break
    
    total=60*m+s
    margin_down=0.9*total
    margin_up=1.1*total
    ans=-1
    m_ans=0
    s_ans=0
    margin=0
    display=""
    for i in range((int(margin_down)+1 if abs(margin_down-int(margin_down))<=0.0000001 else ceil(margin_down)),(int(margin_up) if abs(margin_up-int(margin_up))<=0.0000001 else ceil(margin_up))):
        new_m=i//60
        new_s=i-(i//60)*60
        t=str(new_m).count("9")+str(new_s).count("9")
        time=("0" if len(str(new_m))==1 else "")+str(new_m) + ":"+("0" if len(str(new_s))==1 else "")+str(new_s)
        if t>ans:
            ans=t
            m_ans=new_m
            s_ans=new_s
            margin=abs(total-i)
            display=time
        elif t==ans:
            if margin>abs(total-i):
                m_ans=new_m
                s_ans=new_s
                margin=abs(total-i)
                display=time
            elif margin==abs(total-i) and display>time:
                m_ans=new_m
                s_ans=new_s
                margin=abs(total-i)
                display=time
        if new_s>=60:
            new_m+=1
            new_s-=60
            t=str(new_m).count("9")+str(new_s).count("9")
            time=("0" if len(str(new_m))==1 else "")+str(new_m) + ":"+("0" if len(str(new_s))==1 else "")+str(new_s)
            if t>ans:
                ans=t
                m_ans=new_m
                s_ans=new_s
                margin=abs(total-i)
                display=time
            elif t==ans:
                if margin>abs(total-i):
                    m_ans=new_m
                    s_ans=new_s
                    margin=abs(total-i)
                    display=time
                elif margin==abs(total-i) and display>time:
                    m_ans=new_m
                    s_ans=new_s
                    margin=abs(total-i)
                    display=time
        elif new_s<40 and new_m!=0:
            new_m-=1
            new_s+=60
            t=str(new_m).count("9")+str(new_s).count("9")
            time=("0" if len(str(new_m))==1 else "")+str(new_m) + ":"+("0" if len(str(new_s))==1 else "")+str(new_s)
            if t>ans:
                ans=t
                m_ans=new_m
                s_ans=new_s
                margin=abs(total-i)
                display=time
            elif t==ans:
                if margin>abs(total-i):
                    m_ans=new_m
                    s_ans=new_s
                    margin=abs(total-i)
                    display=time
                elif margin==abs(total-i) and display>time:
                    m_ans=new_m
                    s_ans=new_s
                    margin=abs(total-i)
                    display=time
    print(display)
