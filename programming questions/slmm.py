from collections import deque
from operator import le, ge
class dq(deque):
    def add(self, element):
        return self.append(element)
    def addback(self, element):
        return self.appendleft(element)
    def getfront(self):
        return self[-1]
    def getback(self):
        return self[0]
    def popfront(self):
        return self.pop()
    def popback(self):
        return self.popleft() 
    

def popoutofwindow(q, i, k): 
    if q and q.getback()[0] == i-k:
        q.popback()
        
def deleteUntilInsert(q, i, v, op):
    while q and op(q.getfront()[1], v):
        q.popfront()
    q.add((i,v))
     
def slidingWindowMinMax(arr, k):
    minq = dq()
    maxq = dq()
    r = []
    for i, v in enumerate(arr): 
        for q in [minq,maxq]:
            popoutofwindow(q, i, k) 
        for q, op in [(minq, ge),(maxq, le)]:
            deleteUntilInsert(q,i,v,op) 
        if i >= k-1: #remove this if statement for partial-window case (when you want min/max values from when full window size not reached)
            r.append((minq.getback()[1],maxq.getback()[1]))
            #uncomment lines as per your needs ;)
            #r.append(minq.getback()[1]) #for sliding window minimums
            #r.append(maxq.getback()[1]) #for sliding window maximums
    return r

                
def test(func, case):
    for inp, out in case:
        assert func(*inp) == out, "expected "+str(inp)+" should give output "+str(out)+", got "+str(func(*inp))

testcases = [   
(([1],1), [(1,1)]),
(([1,2,-1,-3,4,2,5,3],3), [(-1, 2), (-3, 2), (-3, 4), (-3, 4), (2, 5), (2, 5)]),
(([5.5, 6.0, 6.0, 6.5, 6.0, 5.5, 5.5, 5.0, 4.5],3), [(5.5, 6.0), (6.0, 6.5), (6.0, 6.5), (5.5, 6.5), (5.5, 6.0), (5.0, 5.5), (4.5, 5.5)]),
(([2,1,3,4,6,3,8,9,10,12,56],4),[(1, 4), (1, 6), (3, 6), (3, 8), (3, 9), (3, 10), (8, 12), (9, 56)]),
(([4,3,2,1,5,7,6,8,9],3), [(2, 4), (1, 3), (1, 5), (1, 7), (5, 7), (6, 8), (6, 9)]),
(([11, -2, 1, 6, 0, 9, 8, -1, 2, 15],3), [(-2, 11), (-2, 6), (0, 6), (0, 9), (0, 9), (-1, 9), (-1, 8), (-1, 15)]), 
]


test(slidingWindowMinMax, testcases)

print("All good!")
