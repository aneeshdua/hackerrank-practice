import sys

def solution(A):
  """Your solution goes here."""
  arr= [[0]*26]*10
  status=[[0]*26]*10
  for i in A:
    s=i[0]
    f=int(i[1])
    r=ord(i[2])-65
    #print(r)
    if(s=='+'):
      arr[f][r]  = arr[f][r]+1
      status[f][r] = 1
    elif(s=='-'):  
      status[f][r] = 0
  max1=0
  floor=0
  room=0
  for i in range(10):
    for j in range(26):
      if(arr[i][j]>max1):
        max1=arr[i][j]
        f=i
        r=j
  print(arr)      
  print(f)
  #print(chr(65+r))      
  res=str(f)+chr(65+r)
  print(res)
  return res


def main():
  # Read from stdin, solve the problem, and write the answer to stdout.
  sys.stdout.write(solution(sys.stdin.readline().split(",")))


if __name__ == "__main__":
  main()
