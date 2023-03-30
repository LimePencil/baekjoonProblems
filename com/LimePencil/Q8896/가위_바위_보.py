import sys

input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n=int(input())
    robots=[]
    lost=[False]*n
    for i in range(n):
        robots.append(input())
    for i in range(len(robots[0])):
        s=set()
        for j in range(n):
            if not lost[j]:
                s.add(robots[j][i])
        if len(s)!=2:
            continue
        elif "R" in s and "P" in s:
            for j in range(n):
                if not lost[j] and robots[j][i]=="R":
                    lost[j]=True
        elif "R" in s and "S" in s:
            for j in range(n):
                if not lost[j] and robots[j][i]=="S":
                    lost[j]=True
        else:
            for j in range(n):
                if not lost[j] and robots[j][i]=="P":
                    lost[j]=True
        cnt=0
        idx=-1
        for j in range(n):
            if not lost[j]:
                cnt+=1
                idx=j+1
        if cnt==1:
            print(idx)
            break
    else:
        print(0)