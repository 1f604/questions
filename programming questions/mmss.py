# Minimal/Maximal sum subarray 
"""
Created on Fri Jun 16 14:25:21 2017

@author: 1f604
"""
import operator 

def max_subarray_sum(A):
    cur = 0
    result = 0
    for v in A:
        cur = max(cur+v,v)
        result = max(result, cur)
    return result 

def min_max_subarray(mode, A, min_subarray_length):
    if mode == "max":
        relate = operator.gt
    elif mode == "min":
        relate = operator.lt
    else:
        return "Accepted modes: min, max"
    cl = 0 #current low. current high is always i
    rl = 0 #result low
    rh = 0 #result high
    if min_subarray_length == 0:
        cur = 0
        result = 0
    elif min_subarray_length == 1:
        cur = A[0]
        result = A[0]
    else:
        return "Accepted values for min_subarray_length: 0, 1"
    for i in range(min_subarray_length,len(A)):
        cur += A[i]
        if relate(A[i],cur):
            cur = A[i]
            cl = i
        if relate(cur,result):
            result = cur
            rl, rh = (cl, i) 
    return (rl, rh, A[rl:rh+1], result)
    

if __name__ == "__main__":
    assert(min_max_subarray("min",[-2, 1, -3, 4, -1, 2, 1, -5, 4], 1) == (7, 7, [-5], -5))
    assert(min_max_subarray("max",[-2, 1, -3, 4, -1, 2, 1, -5, 4], 1) == (3, 6, [4, -1, 2, 1], 6))
    assert(min_max_subarray("max",[-2, -5, 6, -2, -3, 1, 5, -6],1) == (2, 6, [6, -2, -3, 1, 5], 7))
    assert(min_max_subarray("max",[4, -2, -8, 5, -2, 7, 7, 2, -6, 5],1) == (3, 7, [5, -2, 7, 7, 2], 19))
    assert(min_max_subarray("max",[0,-1,2,-3,5,9,-5,10],1) == (4, 7, [5, 9, -5, 10], 19)) 
    print(min_max_subarray("min",[-8, 3, -65, 20, 45, -100, -8, 17, -4, -14],1)) 
    
    
