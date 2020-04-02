class Activity(object):
    def __init__(self,start,finish,index):
        self.start = start
        self.finish = finish
        self.index = index


def testcase(start, finish, n):
    arr = []
    for i in range(n):
        arr.append(Activity(start[i],finish[i],i))
        arr.sort(key=lambda i:i.finish)

    i = 0
    print(int(arr[i].index) + 1, end = " ")
    for j in range(1,len(arr)):
        if (arr[j].start >= arr[i].finish):
            print(int(arr[j].index) + 1, end = " ")
            i = j
    print()
    return

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        start = list(map(int, input().split()))
        finish = list(map(int, input().split()))
        testcase(start, finish, n)
