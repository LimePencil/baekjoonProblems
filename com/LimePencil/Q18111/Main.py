import sys

n,m,b = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
blocks = []
lowest = 256
highest = 0
for _ in range(n):
    row = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
    blocks.append(row)
    lowest = min(lowest,min(row))
    highest = max(highest,max(row))

min_time_taken = 1e10
max_height = -1
for i in range(lowest,highest+1):
    inventory = b
    time_taken = 0
    height = i
    for N in range(n):
        for M in range(m):
            current_height = blocks[N][M]
            if(current_height > height):
                time_taken += 2* (current_height-height)
                inventory +=  (current_height-height)
            elif(current_height < height):
                time_taken += height - current_height
                inventory -= height-current_height
    if(inventory >=0 and time_taken <= min_time_taken):
        max_height = height
        min_time_taken = time_taken
print(str(min_time_taken) + " " + str(max_height))
        
