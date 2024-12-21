### part 1
import utils
lines = utils.get_input_lines()

def sign(num):
    return -1 if num < 0 else 1

def predicate(i, level, sign_):
    diff = level[i] - level[i-1]
    return sign(diff) == sign_ and 0 < abs(diff) < 4

def isvalid(level):
    # check all increasing or all decreasing
    start = level[1] - level[0]
    return all(predicate(i, level, sign(start)) for i in range(1, len(level)))
    

levels = []
for line in lines:
    levels.append([int(z) for z in line.split()])

print(sum([1 if isvalid(level) else 0 for level in levels]))

### part 2
# stupid brute force solution. Surely there must be a more efficient way than trying all permutations.
def permutations(level):
    result = []
    for i in range(len(level)):
        newlevel = level[:]
        del newlevel[i]
        result.append(newlevel)
    return result

total = 0
for level in levels:
    if any(isvalid(perm) for perm in permutations(level)):
        total += 1
print(total)