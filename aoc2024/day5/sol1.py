### part 1
import utils
lines = utils.get_input_lines()

rules:list[tuple[str, str]] = []
updates = []
cur = rules
for line in lines:
    if line == "\n":
        cur = updates
        continue
    if cur == rules:
        cur.append(line.strip().split("|"))
    else:
        cur.append(line.strip().split(","))

def isvalid(update):
    d = {v:i for i,v in enumerate(update)}
    for a, b in rules:
        if a not in d or b not in d:
            continue
        if d[a] > d[b]:
            return False
    return True

total = 0
for update in updates:
    if isvalid(update):
        total += int(update[len(update)//2])
print(total)

### part 2
from collections import defaultdict
import random
ordered_before = defaultdict(set)
# Given an element, return all the elements that are ordered before it due to the rules
for a, b in rules:
    ordered_before[b].add(a)
# I tried ordered_after, it's way too slow with recursive backtracking!!!
# Old logic was to add an item if no elements ordered after it are in the list.

#logic: WE only add an item if all elements ordered before it are already in the list!
def backtrack(cur_list, remaining:set):
    #print("remaining:", len(remaining))
    # pick an elem, if it doesn't work, try again    
    if len(remaining) == 0:
        print("SUccess:", cur_list)
        return cur_list
    candidates = []
    for item in remaining:
        if all(a in cur_list or (a not in cur_list and a not in remaining)
               for a in ordered_before[item]):
            candidates.append(item)
    
    for candidate in candidates:
        result = backtrack(cur_list + [candidate], remaining - {candidate})
        if result:
            return result
    # if all candidates failed, return False
    return False

total = 0
import time
start = time.time()
for update in updates:
    if not isvalid(update):
        # we rebuild the whole thing
        newlist = backtrack([], set(update))
        total += int(newlist[len(newlist)//2])
print(total)
print("Time taken:", time.time() - start)
# Time taken: 0.037236690521240234
