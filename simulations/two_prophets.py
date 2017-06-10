#http://boards.4chan.org/sci/thread/8963892#p8964591

#Two prophets,
#The accuracy of the first person's prophecy is 90%.
#The accuracy of the second person's prophecy is 30%.
#They all predicted the end of the world.
#What's the probability of the end of the world?

#Okay, so we actually have only two possibilities: either they are both wrong or both right.
#If the world ends then they are both right, and the chance of that happening is 0.3 * 0.9 = 27%
#If the world doesn't end then they are both wrong. The chance of that happening is 0.1 * 0.7 = 7%
#So the chance of the world ending is 27 of (27+7), and that is 27/34 ~=~ 79.4%

#The important thing here is that both prophets made the same guess. 

from random import randint 

A_prob = 90
B_prob = 30 

both_correct_count = 0
both_wrong_count = 0

for i in xrange(100000):
    if randint(0,99) < A_prob:
        A_correct = True
    else:
        A_correct = False
    if randint(0,99) < B_prob:
        B_correct = True
    else:
        B_correct = False
    if A_correct and B_correct:
        both_correct_count += 1
    if not A_correct and not B_correct:
        both_wrong_count += 1
        
print both_correct_count, both_wrong_count, both_correct_count/float(both_correct_count+both_wrong_count)
