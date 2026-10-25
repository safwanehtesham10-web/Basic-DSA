def merge_sorted_lists(left_list, right_list):
    p1, p2 = 0, 0
    combined = []
    while p1 < len(left_list) and p2 < len(right_list):
        if left_list[p1] <= right_list[p2]:
            combined.append(left_list[p1])
            p1 += 1
        else:
            combined.append(right_list[p2])
            p2 += 1
    while p1 < len(left_list):
        combined.append(left_list[p1])
        p1 += 1
    while p2 < len(right_list):
        combined.append(right_list[p2])
        p2 += 1
    return combined

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
