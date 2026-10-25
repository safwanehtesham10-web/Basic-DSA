def get_occurrence_count(sorted_list, key):
    total = 0
    for val in sorted_list:
        if val == key:
            total += 1
        elif val > key:
            break
    return total

print(get_occurrence_count([1, 2, 2, 2, 3], 2))
