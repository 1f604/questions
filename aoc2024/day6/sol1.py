### part 1
import utils
lines = utils.get_input_lines()

from collections import defaultdict

coords, mat = utils.getmat(lines, "|")

for x, y in coords:
    if mat[x,y] == "^":
        gx, gy = x, y

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
