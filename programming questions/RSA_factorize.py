# Factor N given e and d
# Requires square_and_multiply.py to be in the same directory. 
"""
Created on Wed Jun 14 22:28:59 2017

@author: 1f604
"""

import random
from square_and_multiply import RLE

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

def find_root(N, e, d):
    k = e * d - 1   
    while(True):
        a = random.randint(1,N)
        if not coprime(a, N):
            continue 
        t = k
        while t % 2 == 0: 
            t /= 2
            x = RLE(a, t, N) 
            if x == N - 1: 
                break
            if x != 1:
                return x
                
def find_pq(N,e,d):
    x = find_root(N,e,d)
    p = gcd(x-1, N) 
    return set((p,N/p))
    

if __name__ == "__main__":
    assert(find_pq(55,3,27)=={5,11})
    assert(find_pq(25777,3,16971)=={149,173})
    n = int('0xa66791dc6988168de7ab77419bb7fb0c001c62710270075142942e19a8d8c51d053b3e3782a1de5dc5af4ebe99468170114a1dfe67cdc9a9af55d655620bbab',16)
    e = int('10001',16)
    d = int('0x123c5b61ba36edb1d3679904199a89ea80c09b9122e1400c09adcf7784676d01d23356a7d44d6bd8bd50e94bfc723fa87d8862b75177691c11d757692df8881',16)
    p,q = (find_pq(n,e,d))
    assert({hex(p),hex(q)}=={'0x33d48445c859e52340de704bcdda065fbb4058d740bd1d67d29e9c146c11cf61L', '0x335e8408866b0fd38dc7002d3f972c67389a65d5d8306566d5c4f2a5aa52628bL'})
    
