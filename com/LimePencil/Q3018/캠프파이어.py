import sys

input = sys.stdin.readline
e = int(input())
n = int(input())
music_cnt=0
people=[set() for _ in range(e+1)]
for _ in range(n):
    people_that_came=list(map(int,input().split()))[1:]
    if 1 in people_that_came:
        music_cnt+=1
        for p in people_that_came:
            people[p].add(music_cnt)
    else:
        songs_they_know=set()
        for p in people_that_came:
            songs_they_know= songs_they_know.union(people[p])
        for p in people_that_came:
            people[p]=set(songs_they_know)
for i,p in enumerate(people):
    if len(p)==music_cnt:
        print(i)