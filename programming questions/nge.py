#Next greater element

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    
def clamp(i):
    return i if i > 0 else -1
         
def nextGreaterDict(A):
    stack = Stack()
    result = {}
    for i, v in enumerate(A):
        while not stack.isEmpty() and v > stack.peek()[1]:
                si,sv = stack.pop()
                result[si] = (i,v) 
        stack.push((i,v))
    while not stack.isEmpty(): 
        si,sv = stack.pop()
        result[si] = (-1,-1)
    return result
         
def nextGreater(A):
    d = nextGreaterDict(A) 
    r = []
    for i in range(len(A)): 
        r.append(d[i][1])
    return r
    
def distanceToNextGreater(A):
    d = nextGreaterDict(A) 
    r = []
    for i in range(len(A)): 
        r.append(clamp(d[i][0]-i))
    return r
                
                
def test(func, case):
        for inp, out in case:
            assert func(inp) == out, "expected "+str(inp)+" should give output "+str(out)

testcases1 = [   
([1], [-1]),
([4, 5, 2, 10], [5, 10, 10, -1]),
([11,13,21,3],[13, 21, -1, -1]),
([13, 7, 6, 12],[-1, 12, 12,-1]),
([5, 9, 3, 5, 4],[9, -1, 5, -1, -1]),
([3, 2, 1], [-1, -1, -1] ),
([40,50,11,32,55,68,75],[50,55,32,55,68,75,-1] ),
([4, 15, 2, 9, 20, 11, 13] , [15, 20, 9, 20, -1, 13, -1] )
]

testcases2 = [  
([1],[-1]),
([4, 5, 2, 10],[1,2,1, -1]),
([11,13,21,3],[1, 1, -1, -1]),
([13, 7, 6, 12], [-1, 2, 1,-1]),
([5, 9, 3, 5, 4], [1, -1, 1, -1, -1]),
([3, 2, 1], [-1, -1, -1] ),
([40,50,11,32,55,68,75], [1,3,1,1,1,1,-1]),
([4, 15, 2, 9, 20, 11, 13] , [1, 3, 1, 1, -1, 1, -1] )
]

test(nextGreater, testcases1)
test(distanceToNextGreater, testcases2) 

print("All good!")
