### part 1
import utils
lines = utils.get_input_lines()

# idea: we go through the matrix, finding occurrences of X
# When we find X, we try to find MAS in all 8 directions
# simple brute force way

class Matrix:
    def __init__(self, mat):
        self.mat = mat
    
    def getd(self, row, col, default):
        """ Returns mat[row][col] or default if out of bounds """
        if row < 0 or row >= len(self.mat):
            return default
        if col < 0 or col >= len(self.mat[row]):
            return default
        return self.mat[row][col]

    def getn(self, basex, basey, addx, addy, length, default):
        return [self.getd(basex + addx*i, basey + addy*i, default) for i in range(length)]

    def getx(self, basex, basey, addx, addy, length, default):
        x1 = self.getn(basex, basey, addx, addy, length, default)
        x2 = self.getn(basex, basey, -addx, -addy, length, default)
        return list(reversed(x2)) + x1[1:]


mat = Matrix(lines)

total = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if mat.getd(row, col, ' ') == 'X':
            for addx, addy in (
                (x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)
            ):
                line = mat.getn(row, col, addx, addy, 4, ' ')
                if line == ['X', 'M', 'A', 'S']:
                    total += 1

print(total)

### part 2

total = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if mat.getd(row, col, ' ') == 'A':
            count = 0
            for addx, addy in [(1, 1), (-1, 1)]:
                line = mat.getx(row, col, addx, addy, 2, ' ')
                if line == ['M', 'A', 'S'] or line == ['S', 'A', 'M']:
                    count += 1
            if count == 2:
                total += 1

print(total)

