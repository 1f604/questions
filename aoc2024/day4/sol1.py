# This solution doesn't work.

### part 1
import utils
lines = utils.get_input_lines()

# idea: we go through the matrix, finding occurrences of X
# When we find X, we try to find MAS in all 8 directions
# simple brute force way
from collections import defaultdict
height = len(lines)
width = len(lines[0])

def get_range(start, reverse=False):
    if not reverse:
        return list(range(start, start + 4))
    else:
        return list(reversed(range(start - 3, start + 1)))

def isvalid(r, c):
    if not 0 <= r < height:
        return False
    if not 0 <= c < width:
        return False
    return True

def get_elems(start_r, reversed_r, start_c, reversed_c) -> list[int]:
    rs = get_range(start_r, reversed_r)
    cs = get_range(start_c, reversed_c)
    elems = []
    for r, c in zip(rs, cs):
        if not isvalid(r, c):
            return []
        else:
            elems.append((r, c))
    return elems        

def countat(lines, row, col) -> int:
    s = {}
    # 1-2: horizontals
    s[1] = lines[row][col:col+4]
    s[2] = lines[row][col-3:col+1]
    # 3-4: verticals
    s[3] = [lines[r][col] if r < height else None for r in range(row, row+4)]
    s[4] = [lines[r][col] if r >= 0 else None for r in range(row-3, row+1)]
    # 5-8: diagonals
    # both +ve
    s[5] = get_elems(row, True, col, True)
    s[6] = get_elems(row, True, col, False)
    s[7] = get_elems(row, False, col, True)
    s[8] = get_elems(row, False, col, False)
    count = 0
    for k, v in s.items():
        if v == ['X', 'M', 'A', 'S']:
            count += 1
    return count



total = 0
for row in range(height):
    for col in range(width):
        char = lines[row][col]
        if char == 'X':
            # do the search
            total += countat(lines, row, col)
print(total)
