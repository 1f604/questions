# authored on: 21 Dec 2024
### part 1
import time, utils
lines = utils.get_input_lines()

from collections import defaultdict

coords, mat = utils.getmat(lines, "|")

for x, y in coords:
    if mat[x,y] == "^":
        gx, gy = x, y
saved_gx, saved_gy = gx, gy

rotate = {
    (0, 1):   (1, 0),
    (1, 0):   (0, -1),
    (0, -1):  (-1, 0),
    (-1, 0):  (0, 1),
}

visited = set([(gx, gy)])
visited_blocks = set()
jump_table = {}
dx, dy = 0, 1
prev_block = (gx, gy, dx, dy)
while True:
    if mat[gx + dx, gy + dy] == "|":
        # if we walk out the map, then end
        break
    elif mat[gx + dx, gy + dy] == "#":
        # add to jump table
        block = (gx, gy, dx, dy)
        jump_table[prev_block] = block
        prev_block = block
        # turn 90 degrees
        dx, dy = rotate[dx, dy]
    else:
        gx, gy = gx+dx, gy+dy
        visited.add((gx, gy))
    #print(len(visited))
print(len(visited))

### part 2
# authored on: 22 Dec 2024
# stupid brute force solution
# but now using Boojum's jump table idea
def is_blocked(x1, y1, ox, oy):
    return x1 == ox or y1 == oy

def is_blocked2(x1, y1, dx, dy, ox, oy, x2, y2):
    if dx == 0:
        if dy == -1:
            return y1 > oy > y2
        if dy == 1:
            return y1 < oy < y2
    elif dy == 0:
        if dx == -1:
            return x1 > ox > x2
        if dx == 1:
            return x1 < ox < x2

#print(jump_table)
def try_mat(ox, oy):
    gx, gy = saved_gx, saved_gy
    dx, dy = 0, 1
    visited_blocks = set()
    while True:
        if mat[gx + dx, gy + dy] == "|":
            # if we walk out the map, then end
            return False
        elif mat[gx + dx, gy + dy] == "#":
            block = (gx, gy, dx, dy)
            if block in visited_blocks:
                return True
            visited_blocks.add(block)
            if block in jump_table and not is_blocked(gx, gy, ox, oy):
                gx, gy, dx, dy = jump_table[block]
                continue
            # turn 90 degrees
            dx, dy = rotate[dx, dy]
        else:
            gx, gy = gx+dx, gy+dy
        #print(gx, gy)

total = 0
start = time.time()
for x, y in visited:
    if mat[x,y] == '.':
        mat[x, y] = '#'
        if try_mat(x, y):
            total += 1
        mat[x, y] = '.'
    
print(total)
print("time taken:", time.time() - start)
# time taken: 0.5551228523254395