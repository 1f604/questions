#Sum numbers in an array:

def  sumOfIntegers( arr): #hmm...
    sum = 0
    for i in arr:
        sum+=i
    return sum

arr = [1,2,3]
print sum(arr)
print sumOfIntegers(arr)