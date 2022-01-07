try:
    range_min = int(input('insert floor'))
except ValueError:
    range_min = None

try:
    range_max = int(input('insert ceil'))
except ValueError:
    range_max = None


print(range_min, range_max)


