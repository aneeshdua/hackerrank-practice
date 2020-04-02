t = int(input())
for i in range(t):
    s = input().split()
    x1 = int(s[0])
    x2 = int(s[1])
    n = x2-x1
    sqt_n = n**0.5
    prime = [True for j in range(100000)]
    p=2
    while(p*p<=n):
        if(prime[p]==True):
            for x in range(p*p, n+1,p):
                prime[x] = False
        p+=1
    for p in range(2,n):
        if prime[p]:
            print(p)
            #print('\n')
    #print('\n')        
