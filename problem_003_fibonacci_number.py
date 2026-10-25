def get_fibonacci(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return get_fibonacci(k - 1) + get_fibonacci(k - 2)

print(get_fibonacci(6))
