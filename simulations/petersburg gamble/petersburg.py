#written on 8th November 2015
n=20
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
for k in range(50):
    ls = []
    for j in range(5000):
        total = 0
        for i in range(n):
            total+=toss()
        ls.append(total/n)
    mean = sum(ls) / len(ls)
    median = ls[len(ls)//2]
    stdv = math.sqrt(sum((mean - value) ** 2 for value in ls) / len(ls))
    means.append(math.floor(mean))
    medians.append(math.floor(median))
    stdvs.append(math.floor(stdv))


print("Stats of 5,000 20-game-long-trial averages:")
print("medians: "+str(medians))
print("If you see a median of 500 it means the median of 5,000 20-game-long-trial means was 500.")
print("mean of medians: "+str(sum(medians)/len(medians)))
print("median of medians: "+str(medians[len(medians)//2]))
print("If the median of medians is 5, it means that if you play the game 20 times, you are likely to win $5 per game on average")
print("means: "+str(means))
print("mean of means: "+str(sum(means)/len(means)))
print("median of means: "+str(means[len(means)//2]))
print("standard deviations: "+str(stdvs))