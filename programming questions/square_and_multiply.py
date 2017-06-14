#exponentiation by square & multiply
"""
Created on Wed Jun 14 15:57:39 2017

@author: 1f604
""" 
import cProfile

def to_bits(n): #this method is quite inefficient
    bits = []
    while(n):
        bits.append(n%2)
        n /= 2 
    return list(reversed(bits))

def to_bits2(n): #this method is even more inefficient
    return [int(x) for x in bin(n)[2:]]
    
def LRE(base,exponent,modulus):
    bits = to_bits(exponent)[1:] # ignore the highest bit 
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

def boo():
    for i in range(100000):
        assert(LRE(9688563,4589905674336394257982673890276389348996756,71)==30) 

def hoo():
    for i in range(100000):
        assert(RLE(9688563,4589905674336394257982673890276389348996756,71)==30) 

if __name__ == "__main__":
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
    cProfile.run('boo()')
    cProfile.run('hoo()')
