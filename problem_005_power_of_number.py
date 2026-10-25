def calc_power(base, exp):
    if exp == 0:
        return 1
    return base * calc_power(base, exp - 1)

print(calc_power(2, 3))
