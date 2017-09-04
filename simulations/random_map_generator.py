#python 2.7
from hashlib import md5
import random
rows = 50
columns = 50
mat = [[1 for x in range(columns)] for y in range(rows)]
seed = random.randint(0,100000)
def check(r,c):
    return sum(bytearray(md5(str(seed)+str(r)+' '+str(c)).hexdigest())) % 12 >= 11
def checkrange(r,c):
    prob = 0
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if check(i,j):
                prob += 2
    if random.randint(0,prob) > 0:
        if prob > 2:
            return 8
        else:
            return 3
    return 1
for r in range(rows):
    for c in range(columns):
        if check(r,c):
            mat[r][c] = 8
        elif r > 0 and r < rows-1 and c > 0 and c < columns-1:
            mat[r][c] = checkrange(r,c)
    
for r in mat:
    print r
