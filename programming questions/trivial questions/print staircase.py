'''
Problem:

Given an integer n, print n lines consisting of whitespace and # symbols, with the number of # symbols increasing from 1 to n each line, each line has a total of n characters.  

Example: 
Input: 4
Output:
   #
  ##
 ###
 ####
 
Solution:
'''

l = int(raw_input())
for i in range(1,l+1):
    print " "*(l-i)+"#"*i
	
#Interestingly my answer is identical to the stackoverflow answer: http://stackoverflow.com/questions/31222291/hackerrank-staircase-python I guess there aren't many ways to do this question lol. 