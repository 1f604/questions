### part 1
import utils
lines = utils.get_input_lines()

haystack = "".join(lines)
import re
# mul(X,Y), where X and Y are each 1-3 digit numbers. 
patstr = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
reg = re.compile(patstr)
matches = reg.findall(haystack)
total = 0
for match in matches:
    xy = match[4:-1]
    x, y = [int(s) for s in xy.split(",")]
    total += x*y
print(total)

### part 2

reg = re.compile(r"(?:mul\([0-9]{1,3},[0-9]{1,3}\))|(?:don't\(\))|(?:do\(\))")
matches = reg.findall(haystack)
total = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        xy = match[4:-1]
        x, y = [int(s) for s in xy.split(",")]
        if enabled:
            total += x*y
print(total)
