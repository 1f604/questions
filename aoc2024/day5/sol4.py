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
ordered_before = defaultdict(set)
# Given an element, return all the elements that are ordered before it due to the rules
for a, b in rules:
    ordered_before[b].add(a)
# I tried ordered_after, it's way too slow with recursive backtracking!!!
# Old logic was to add an item if no elements ordered after it are in the list.

import functools
def compare(a,b):
    return 1 if b in ordered_before[a] else -1 if a in ordered_before[b] else 0

import time
start = time.time()
total = 0
for update in updates:
    if not isvalid(update):
        update.sort(key=functools.cmp_to_key(compare))
        total += int(update[len(update)//2])
print(total)
print("Time taken:", time.time() - start)
# Time taken: 0.009236335754394531
