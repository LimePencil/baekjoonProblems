for i in range(100,1000):
    for j in range(100,1000):
        if i%10==j//100 and j%100!=0 and i/(i//10)==j/(j%100) and not (i==j and i%111==0):
                print(f"{i} / {j} = {i//10} / {j%100}")