import sys
from itertools import permutations
from collections import deque
def chord_to_int(s:str):
    return ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"].index(s)

input = lambda: sys.stdin.readline().rstrip()
n,j = list(map(int,input().split()))
tune= list(map(chord_to_int,input().split()))
chord= list(map(chord_to_int,input().split()))

m=float('inf')
for p in permutations(range(n),j):
    l=[]
    for k,e in enumerate(p):
        if chord[k]>tune[e]:
            l.append((chord[k]-tune[e]))
        elif chord[k]==tune[e]:
            continue
        else:
            l.append((chord[k]+12-tune[e]))
    if len(l)>0:
        l.sort()
        l=deque(l)
        cnt=0
        while len(l)!=1 and l[-1]-l[0]>=l[0]+12-l[1] and cnt<7:
            a=l.popleft()
            l.append(a+12)
            cnt+=1
        m=min(l[-1]-l[0]+1,m)
    else:
        m=0
        break
         
print(m)