#popcount for 32 bit numbers in python (kind of pointless, I know)
#Created on Tue May 30 2017  

def popcount(v):
    v = v - ((v>>1) & 0b01010101010101010101010101010101)
    v = (v & 0b00110011001100110011001100110011) + ((v>>2) & 0b00110011001100110011001100110011);
    v = v + (v >> 4) & 0x0F0F0F0F
    v = v * 0x01010101
    v = v >> 24
    return v&0b11111111
print(popcount(eval(input("Please enter a number:"))))
