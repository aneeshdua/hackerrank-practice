def bell_number(n,k):
    if(n==0 or k==0 or k>n):
        return 0
    if(k==1 or k==n):
        return 1
    return (k * bell_number(n - 1, k) + bell_number(n - 1, k - 1))
n = int(input())
count=0
for i in range(1,n+1):
    count = count+bell_number(n,i)
print(count)
