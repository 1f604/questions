# For context, see https://1f604.blogspot.com/2023/01/sets-with-distinct-subset-sums.html

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    
def check(x):
    ps = powerset(x)
    sums = {} # dict of sum(subset) -> subset
    for subset in ps:
    	s = sum(subset)
    	if s in sums:
    		#print(x, "Fail. Duplicate:", sums[s], "==", subset)
    		return False
    	sums[s] = subset
    #print(x, "Success!")
    return True
   
def check_with_print(x):
    ps = powerset(x)
    sums = {} # dict of sum(subset) -> subset
    for subset in ps:
    	s = sum(subset)
    	if s in sums:
    		print(x, "Fail. Duplicate:", sums[s], "==", subset)
    		return False
    	sums[s] = subset
    print(x, "Success!")
    return True
    
check_with_print([1,2,3])
check_with_print([1,2,4])
check_with_print([1,2,4,7,9])
check_with_print([1,2,4,8,16])
check_with_print([6,9,11,12,13])

							
import itertools
for comb in itertools.combinations(list(range(1,25)), 6):
	if check(comb):
		print(comb)
