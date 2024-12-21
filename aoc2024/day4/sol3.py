# Inspired by 4HbQ's solution

### part 1
import utils
lines = utils.get_input_lines()

# idea: we go through the matrix, finding occurrences of X
# When we find X, we try to find MAS in all 8 directions
# simple brute force way
from collections import defaultdict

mat = defaultdict(lambda: " ")
for row in range(len(lines)):
    for col in range(len(lines[row])):
        mat[row, col] = lines[row][col]

D = -1, 0, 1
coords = list(mat.keys())

total = 0
for i, j in coords:
    if mat[i,j] == 'X':
        total += sum(line == ['X', 'M', 'A', 'S'] for line in [[mat[i + di * n, j + dj * n] for n in range(4)] for di in D for dj in D])

print(total)

### part 2
total = 0
T = [list("MAS"), list("SAM")]
for i, j in coords:
    if mat[i,j] == 'A':
        total += [mat[i + d, j + d] for d in D] in T and [mat[i+d, j-d] for d in D] in T
print(total)