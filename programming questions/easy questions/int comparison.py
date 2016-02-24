#Compare two nonnegative integers (arbitrary size) without using any comparison operators

a = input("Enter the first number")
b = input("Enter the second number")

def assign_compare(a,b): #dict-based implementation inspired by the array-based implementation in the paper "mov is Turing-complete" http://www.cl.cam.ac.uk/~sd601/papers/mov.pdf
    d = {}
    d[a] = "a is not equal to b"
    d[b] = "a is equal to b"
    return d[a]

def isNonZero(a): #OR-based implementation using bitshifting to check if any bits in the number is set
    lena = len(bin(a))-2
    b = 0
    for i in range(lena):
        b |= (a >> i) & 1
    return b

def xor_compare(a,b): #XOR based implementation based on the fact that two identical numbers when XOR'd gives zero, otherwise the result is nonzero
    d = ["a is equal to b","a is not equal to b"]
    c = a ^ b
    return d[isNonZero(c)]

print assign_compare(a,b)
print xor_compare(a,b)