def get_floor_ceil(items, target):
    flr, cl = -1, -1
    for item in items:
        if item <= target:
            flr = item
        if item >= target and cl == -1:
            cl = item
    return flr, cl

print(get_floor_ceil([1, 2, 4, 6, 8], 5))
