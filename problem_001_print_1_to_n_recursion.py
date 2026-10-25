def display_1_to_n(limit):
    if limit < 1:
        return
    display_1_to_n(limit - 1)
    print(limit, end=" ")

display_1_to_n(5)
