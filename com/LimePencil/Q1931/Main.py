import sys

n = int(sys.stdin.readline().rstrip("\n"))
time_table = []
for _ in range(n):
    s, e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    time_table.append((s,e))
time_table.sort(key=lambda time:time[0])
time_table.sort(key=lambda time:time[1])

total = 1
end = time_table[0][1]

for next in range(1,len(time_table)):
    next_start = time_table[next][0]
    next_end = time_table[next][1]

    if(next_start>=end):
        total +=1
        end = next_end


print(str(total))