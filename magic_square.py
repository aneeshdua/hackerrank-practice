from itertools import permutations, chain

def check_magic(arr):
    r1 = arr[0][0]+arr[0][1]+arr[0][2]
    r2 = arr[1][0]+arr[1][1]+arr[1][2]
    r3 = arr[2][0]+arr[2][1]+arr[2][2]
    c1 = arr[0][0]+arr[1][0]+arr[2][0]
    c2 = arr[0][1]+arr[1][1]+arr[2][1]
    c3 = arr[0][2]+arr[1][2]+arr[2][2]
    diagonal1 = arr[0][0]+arr[1][1]+arr[2][2]
    diagonal2 = arr[0][2]+arr[1][1]+arr[2][0]
    if(diagonal1==diagonal2==r1==r2==r3==c1==c2==c3):
        return 1
    else:
        return 0     

a = [[1,2,3],[4,5,6],[7,8,9]]
for i in (permutations(chain.from_iterable(a))):
    print(i)


#a=[[8, 1, 6], [3, 5, 7], [4, 9, 2]]
f = check_magic(a)
print(f)
