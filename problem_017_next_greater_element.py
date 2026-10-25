def compute_next_greater(elements):
    n = len(elements)
    answers = [-1] * n
    idx_stack = []
    for idx in range(n):
        while idx_stack and elements[idx] > elements[idx_stack[-1]]:
            top_idx = idx_stack.pop()
            answers[top_idx] = elements[idx]
        idx_stack.append(idx)
    return answers

print(compute_next_greater([4, 5, 2, 25]))
