def has_subset_sum(numbers, total, idx=0):
    if total == 0:
        return True
    if idx >= len(numbers) or total < 0:
        return False
    return has_subset_sum(numbers, total - numbers[idx], idx + 1) or has_subset_sum(numbers, total, idx + 1)

print(has_subset_sum([3, 34, 4, 12, 5, 2], 9))
