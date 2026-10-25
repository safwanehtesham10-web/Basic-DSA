def calculate_digit_sum(val):
    if val < 10:
        return val
    return (val % 10) + calculate_digit_sum(val // 10)

print(calculate_digit_sum(1234))
