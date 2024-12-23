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
dx, dy = 0, 1
while True:
    if mat[gx + dx, gy + dy] == "|":
        # if we walk out the map, then end
        break
    elif mat[gx + dx, gy + dy] == "#":
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
def try_mat():
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
            # turn 90 degrees
            dx, dy = rotate[dx, dy]        
        else:
            gx, gy = gx+dx, gy+dy

total = 0
start = time.time()
for x, y in visited:
    if mat[x,y] == '.':
        mat[x, y] = '#'
        if try_mat():
            total += 1
        mat[x, y] = '.'
    
print(total)
print("time taken:", time.time() - start)
# try visited only: time taken: 5.41077446937561
# try all cells: time taken: 25.83567500114441