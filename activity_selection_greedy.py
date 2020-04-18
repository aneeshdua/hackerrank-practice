#code
class activity:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
t = int(input())
for z in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    finish = list(map(int, input().split()))
    act=[]
    for i in range(n):
        temp = activity(start[i], finish[i])
        act.append(temp)
    act.sort(key = lambda i:i.finish)
    count=1
    temp = act[0].finish
    for i in range(1,n):
        if(act[i].start>=temp):
            count = count+1
            temp = act[i].finish
    print(count)        