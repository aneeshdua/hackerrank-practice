def climbingLeaderboard(scores, alice):
    res=[]
    sc = list(set(scores))
    sc.sort()
    sc.reverse()
    print(sc)
    for i in alice:
        count=0
        for j in sc:
            #print("i  ",i)
            #print("j  ",j)
            if(i>j):
                count = count + 1
                break
            elif(i==j):
                #print("asd")
                count = count + 1
                break
            count = count+1
        if(count==len(sc)):
            count+=1
        res.append(count)        
    return res

scores = [100,100,50 ,40, 40, 20, 10]
alice = [5, 25 ,50 ,120]
x = climbingLeaderboard(scores,alice)
print(x)
