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
        broken_rules = find_broken_rules(update)
        while broken_rules:
            for a, b in broken_rules:
                # swap a and b
                ia, ib = update.index(a), update.index(b)
                if ia > ib: # this check is necessary since some previously broken rules might no longer be broken after we do this.
                    update[ia], update[ib] = b, a
            broken_rules = find_broken_rules(update)
        total += int(update[len(update)//2])
print(total)
print("Time taken:", time.time() - start)
# Time taken: 0.14911913871765137
