#exponentiation by square & multiply
"""
Created on Wed Jun 14 15:57:39 2017

@author: 1f604
""" 

def to_bits(n):
    bits = []
    while(n):
        bits.append(n%2)
        n = n / 2
    return bits

def LRE(base,exponent,modulus):
    bits = to_bits(exponent)
    bits = list(reversed(bits))[1:] # ignore the highest bit 
    result = base
    for b in bits:
        result *= result
        result %= modulus
        if b: 
            result *= base
            result %= modulus
    return result % modulus

def RLE(base,exponent,modulus):
    result = 1
    term = base 
    while(exponent): 
        bit = exponent % 2
        if bit:
            result *= term
            result %= modulus
        exponent /= 2
        term *= term
        term %= modulus
    return result

assert(LRE(0,1,1)==0) 
assert(RLE(0,1,1)==0) 
assert(LRE(1,1,1)==0) 
assert(RLE(1,1,1)==0) 
assert(LRE(1,1,2)==1) 
assert(RLE(1,1,2)==1) 
assert(LRE(9688563,45896,71)==20) 
assert(RLE(9688563,45896,71)==20) 
assert(LRE(9688563,4589905674336394257982673890276389348996756,71)==30) 
assert(RLE(9688563,4589905674336394257982673890276389348996756,71)==30) 
