### part 1
import utils
lines = utils.get_input_lines()

rules:list[tuple[str, str]] = []
updates:list[list] = []
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

def find_broken_rules(update:list):
    broken_rules = []
    for a, b in rules:
        if a in update and b in update and update.index(a) > update.index(b):
            broken_rules.append((a,b))
    return broken_rules

total = 0
import time
start = time.time()
for update in updates:
    if not isvalid(update):
        new_list = []
        new_set = set()
        # rebuild by taking nodes that can be taken
        updateset = set(update)
        remaining = set(update)
        while remaining:
            # pick a node from remaining and see if it can be added
            for node in remaining:
                if len(ordered_before[node]) == 0 or all(x in new_set or x not in updateset for x in ordered_before[node]):
                    new_list.append(node)
                    new_set.add(node)
                    remaining.remove(node)
                    break            
        total += int(update[len(update)//2])
print(total)
print("Time taken:", time.time() - start)
# Time taken: 0.019832134246826172
