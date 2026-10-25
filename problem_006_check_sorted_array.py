def check_sorted(data, idx=0):
    if idx >= len(data) - 1:
        return True
    if data[idx] > data[idx + 1]:
        return False
    return check_sorted(data, idx + 1)

print(check_sorted([1, 2, 4, 5]))
