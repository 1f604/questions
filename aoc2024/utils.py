import os 
import inspect

def get_input_lines() -> list[str]:
    """ Get lines from the file input.txt """
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    dir_path = os.path.dirname(os.path.realpath(filename))
    with open(dir_path+"/input.txt") as f:
        lines = f.readlines()
    return lines

from collections import defaultdict
def getmat(lines, default) -> tuple[list, dict]:
    """ Returns a matrix with true (x,y) coordinates, not (row, col) coordinates. """
    mat = defaultdict(lambda: default)
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            # mat[x, y] maps to...
            x = col
            y = len(lines)-1-row
            mat[x, y] = lines[row][col]
    coords = list(mat.keys())
    return coords, mat
