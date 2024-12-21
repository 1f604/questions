### part 1
import utils
lines = utils.get_input_lines()

xs = []
ys = []
for line in lines:
    x, y = [int(z) for z in line.split()]
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()

print(sum([abs(x-y) for x,y in zip(xs, ys)]))

### part 2

from collections import Counter

cx = Counter(xs)
cy = Counter(ys)

total = 0
for x in set(xs):
    total += x * cy[x]

print(total)