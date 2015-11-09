#written on 8th November 2015
n=100000000
import random
import math
def toss():
    sum=2
    while(True):
        if(random.randint(0,1)==0):
            return sum
        else:
            sum*=2

medians=[]
stdvs=[]
means=[]
k=1
while(k<n):
    k*=2
    total = 0
    for j in range(k):
        total+=toss()
    mean = total/k
    print("for "+str(k)+" trials of the game, the mean amount won per trial is: "+str(mean))