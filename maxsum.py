#maxmimm sum of numbers
import heapq
def maxsum(arr):
    n=len(arr)
    array=[-1*i for i in arr]
    heapq.heapify(array)
    s1 ,s2=0 ,0
    i=0
    
    while array:
        d=heapq.heappop(array)
        d= -1 * d
        if i==n -1 :
            s2=d
            break
        s1=s1*10+d
        i=i+1
    return s1+s2
   
       
array1=[3,5,2,4,1]
print(maxsum(array1))
