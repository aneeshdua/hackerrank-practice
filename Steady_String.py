t = int(input())
arr = list(map(int,input().split()))
head=len(arr)-1
tail=0
s=0
d=0
while(tail!=head and tail<head):
    if(arr[tail]>arr[head]):
        s+=arr[tail]
        tail+=1
    elif(arr[tail]<=arr[head]):
        s+=arr[head]
        head-=1
    print(s)    
    if(arr[tail]>arr[head]):
        d+=arr[tail]
        tail+=1
    elif(arr[tail]<=arr[head]):
        d+=arr[head]
        head-=1
    print(d)
if(tail==head):
    s+=arr[head]            
print(s," ",d)
    
                