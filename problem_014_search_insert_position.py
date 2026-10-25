def locate_insert_index(values, key):
    start, end = 0, len(values) - 1
    while start <= end:
        center = (start + end) // 2
        if values[center] == key:
            return center
        elif values[center] < key:
            start = center + 1
        else:
            end = center - 1
    return start

print(locate_insert_index([1, 3, 5, 6], 4))
