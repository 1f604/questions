#python 2.7
import matplotlib.pyplot as plt
import numpy as np
from hashlib import md5
import random
rows = 150
columns = 150
mat = [[1 for x in range(columns)] for y in range(rows)]
seed = random.randint(0,100000)
def check(r,c):
    return sum(bytearray(md5(str(seed)+str(r)+' '+str(c)).hexdigest())) % 50 >= 49
def checkrange(r,c):
    prob = 0
    for i in range(r-2,r+3):
        for j in range(c-2,c+3):
            if check(i,j):
                prob += 2
    if random.randint(0,prob) > 1:
        if prob > 2:
            return 8
        else:
            return 3
    return 1
for r in range(rows):
    for c in range(columns):
        if check(r,c):
            mat[r][c] = 8
        elif r > 0 and r < rows-2 and c > 0 and c < columns-2:
            mat[r][c] = checkrange(r,c)
    
for r in mat:
    print r
    
plt.imshow(mat, cmap='hot', interpolation='nearest')
plt.show()
