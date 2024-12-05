import heapq
def findsum(arr):
    s1=s2=0
    l=len(arr)
    for i in range(l):
        d=heapq.heappop(arr)
        if i%2==0:
            s1=s1*10 + d
        else:
            s2=s2*10 + d
    return s1 + s2
array=[1,2,3,4,5]
print(findsum(array))
